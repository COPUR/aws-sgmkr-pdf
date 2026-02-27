#!/usr/bin/env python3
"""
Convert one or more PDFs into markdown with inline image references.

Output for each PDF:
- <output>/<pdf_stem>/document.md
- <output>/<pdf_stem>/images/page-XXXX-img-YY.<ext>
- <output>/<pdf_stem>/manifest.json
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import multiprocessing
import os
import platform
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import fitz  # type: ignore
except ImportError:  # pragma: no cover
    fitz = None


@dataclass(frozen=True)
class ChunkTask:
    pdf_path: str
    doc_out_dir: str
    temp_pages_dir: str
    start_page: int
    end_page: int
    min_width: float
    min_height: float
    min_area: float
    image_dpi: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Extract text and diagram-like images from PDFs and create markdown "
            "with image references for ML preprocessing."
        )
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to a single PDF file or a directory containing PDF files.",
    )
    parser.add_argument(
        "--output-dir",
        default="ml-output",
        help="Directory where converted outputs will be written.",
    )
    parser.add_argument(
        "--pattern",
        default="*.pdf",
        help="File glob when --input points to a directory (default: *.pdf).",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="When --input is a directory, search recursively.",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=0,
        help="Maximum number of pages to process per PDF (0 = all pages).",
    )
    parser.add_argument(
        "--min-image-width",
        type=float,
        default=100.0,
        help="Filter out extracted image blocks narrower than this value.",
    )
    parser.add_argument(
        "--min-image-height",
        type=float,
        default=100.0,
        help="Filter out extracted image blocks shorter than this value.",
    )
    parser.add_argument(
        "--min-image-area",
        type=float,
        default=15000.0,
        help="Filter out extracted image blocks with smaller area than this value.",
    )
    parser.add_argument(
        "--image-dpi",
        type=int,
        default=180,
        help="DPI for rasterizing inline/non-xref image blocks.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=0,
        help=(
            "Number of parallel worker processes per PDF. "
            "0 = auto tuned for local machine."
        ),
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=16,
        help="How many pages each worker task processes at once.",
    )
    parser.add_argument(
        "--keep-temp-pages",
        action="store_true",
        help="Keep intermediate per-page markdown files for debugging.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing output folders if they already exist.",
    )
    return parser.parse_args()


def discover_pdfs(path: Path, pattern: str, recursive: bool) -> list[Path]:
    if path.is_file():
        if path.suffix.lower() != ".pdf":
            raise ValueError(f"Input file is not a PDF: {path}")
        return [path]
    if not path.is_dir():
        raise ValueError(f"Input path does not exist: {path}")
    if recursive:
        return sorted(path.rglob(pattern))
    return sorted(path.glob(pattern))


def safe_text_from_block(block: dict[str, Any]) -> str:
    lines: list[str] = []
    for line in block.get("lines", []):
        spans = line.get("spans", [])
        text = "".join(span.get("text", "") for span in spans).strip()
        if text:
            lines.append(text)
    return "\n".join(lines).strip()


def auto_worker_count() -> int:
    cpu_count = os.cpu_count() or 4
    if platform.system() == "Darwin" and platform.machine() in {"arm64", "aarch64"}:
        # Keep headroom for macOS and foreground tasks.
        return max(1, min(8, cpu_count - 2))
    return max(1, min(6, cpu_count - 1))


def save_image_block(
    doc: Any,
    page: Any,
    block: dict[str, Any],
    destination_base: Path,
    image_dpi: int,
) -> Path | None:
    xref = block.get("xref", 0) or 0
    if xref > 0:
        image_data = doc.extract_image(xref)
        image_bytes = image_data.get("image")
        ext = image_data.get("ext", "png").lower()
        if not image_bytes:
            return None
        image_path = destination_base.with_suffix(f".{ext}")
        image_path.write_bytes(image_bytes)
        return image_path

    # Fallback for inline/non-xref image blocks.
    rect = fitz.Rect(block.get("bbox", [0, 0, 0, 0]))
    if rect.is_empty:
        return None
    pix = page.get_pixmap(clip=rect, alpha=False, dpi=image_dpi)
    image_path = destination_base.with_suffix(".png")
    pix.save(str(image_path))
    return image_path


def build_chunk_tasks(
    pdf_path: Path,
    doc_out_dir: Path,
    temp_pages_dir: Path,
    pages_to_process: int,
    chunk_size: int,
    min_width: float,
    min_height: float,
    min_area: float,
    image_dpi: int,
) -> list[ChunkTask]:
    tasks: list[ChunkTask] = []
    for start_page in range(0, pages_to_process, chunk_size):
        end_page = min(start_page + chunk_size, pages_to_process)
        tasks.append(
            ChunkTask(
                pdf_path=str(pdf_path),
                doc_out_dir=str(doc_out_dir),
                temp_pages_dir=str(temp_pages_dir),
                start_page=start_page,
                end_page=end_page,
                min_width=min_width,
                min_height=min_height,
                min_area=min_area,
                image_dpi=image_dpi,
            )
        )
    return tasks


def process_page_chunk(task: ChunkTask) -> dict[str, Any]:
    doc = fitz.open(task.pdf_path)
    doc_out_dir = Path(task.doc_out_dir)
    images_dir = doc_out_dir / "images"
    temp_pages_dir = Path(task.temp_pages_dir)

    image_count = 0
    images_meta: list[dict[str, Any]] = []

    try:
        for page_index in range(task.start_page, task.end_page):
            page_number = page_index + 1
            page = doc.load_page(page_index)
            page_dict = page.get_text("dict")
            blocks = page_dict.get("blocks", [])
            blocks.sort(key=lambda b: (b.get("bbox", [0, 0])[1], b.get("bbox", [0, 0])[0]))

            page_markdown: list[str] = [f"## Page {page_number}", ""]
            page_image_index = 0

            for block in blocks:
                block_type = block.get("type")
                if block_type == 0:
                    text = safe_text_from_block(block)
                    if text:
                        page_markdown.append(text)
                        page_markdown.append("")
                    continue

                if block_type != 1:
                    continue

                bbox = block.get("bbox", [0, 0, 0, 0])
                width = float(bbox[2] - bbox[0])
                height = float(bbox[3] - bbox[1])
                area = width * height

                if width < task.min_width or height < task.min_height or area < task.min_area:
                    continue

                page_image_index += 1
                image_base = images_dir / f"page-{page_number:04d}-img-{page_image_index:02d}"
                image_path = save_image_block(
                    doc=doc,
                    page=page,
                    block=block,
                    destination_base=image_base,
                    image_dpi=task.image_dpi,
                )
                if image_path is None:
                    continue

                image_count += 1
                rel_image_path = image_path.relative_to(doc_out_dir).as_posix()
                page_markdown.append(
                    f"![Page {page_number} Diagram {page_image_index}]({rel_image_path})"
                )
                page_markdown.append("")

                images_meta.append(
                    {
                        "page": page_number,
                        "index": page_image_index,
                        "path": rel_image_path,
                        "bbox": bbox,
                        "width": width,
                        "height": height,
                        "area": area,
                    }
                )

            page_file = temp_pages_dir / f"page-{page_number:06d}.md"
            page_file.write_text(
                "\n".join(page_markdown).rstrip() + "\n\n",
                encoding="utf-8",
            )
    finally:
        doc.close()

    return {"images": images_meta, "image_count": image_count}


def convert_pdf(
    pdf_path: Path,
    output_dir: Path,
    max_pages: int,
    min_width: float,
    min_height: float,
    min_area: float,
    image_dpi: int,
    workers: int,
    chunk_size: int,
    keep_temp_pages: bool,
    overwrite: bool,
) -> tuple[Path, int, int, int]:
    if chunk_size < 1:
        raise ValueError("--chunk-size must be >= 1")

    doc_name = pdf_path.stem
    doc_out_dir = output_dir / doc_name
    images_dir = doc_out_dir / "images"
    temp_pages_dir = doc_out_dir / ".tmp_pages"
    markdown_path = doc_out_dir / "document.md"
    manifest_path = doc_out_dir / "manifest.json"

    if doc_out_dir.exists():
        if overwrite:
            shutil.rmtree(doc_out_dir)
        else:
            raise FileExistsError(
                f"Output already exists: {doc_out_dir}. Use --overwrite to replace it."
            )

    doc_out_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)
    temp_pages_dir.mkdir(parents=True, exist_ok=True)

    with fitz.open(str(pdf_path)) as doc:
        pages_to_process = doc.page_count if max_pages <= 0 else min(doc.page_count, max_pages)

    effective_workers = max(1, workers)
    tasks = build_chunk_tasks(
        pdf_path=pdf_path,
        doc_out_dir=doc_out_dir,
        temp_pages_dir=temp_pages_dir,
        pages_to_process=pages_to_process,
        chunk_size=chunk_size,
        min_width=min_width,
        min_height=min_height,
        min_area=min_area,
        image_dpi=image_dpi,
    )

    manifest_images: list[dict[str, Any]] = []
    extracted_image_count = 0

    if effective_workers == 1 or len(tasks) == 1:
        for task in tasks:
            result = process_page_chunk(task)
            manifest_images.extend(result["images"])
            extracted_image_count += int(result["image_count"])
    else:
        context = multiprocessing.get_context("spawn")
        with concurrent.futures.ProcessPoolExecutor(
            max_workers=effective_workers,
            mp_context=context,
        ) as executor:
            for result in executor.map(process_page_chunk, tasks):
                manifest_images.extend(result["images"])
                extracted_image_count += int(result["image_count"])

    with markdown_path.open("w", encoding="utf-8") as markdown_file:
        markdown_file.write(f"# {pdf_path.name}\n\n")
        for page_number in range(1, pages_to_process + 1):
            page_file = temp_pages_dir / f"page-{page_number:06d}.md"
            if page_file.exists():
                markdown_file.write(page_file.read_text(encoding="utf-8"))

    manifest_images.sort(key=lambda image: (image["page"], image["index"]))
    manifest = {
        "source_pdf": str(pdf_path.resolve()),
        "page_count": pages_to_process,
        "workers": effective_workers,
        "chunk_size": chunk_size,
        "image_dpi": image_dpi,
        "images": manifest_images,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    if not keep_temp_pages:
        shutil.rmtree(temp_pages_dir, ignore_errors=True)

    return markdown_path, pages_to_process, extracted_image_count, effective_workers


def main() -> int:
    args = parse_args()
    if fitz is None:
        print(
            "Missing dependency: PyMuPDF.\n"
            "Install it with: python3 -m pip install -r requirements.txt",
            file=sys.stderr,
        )
        return 2

    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()

    try:
        pdf_paths = discover_pdfs(input_path, args.pattern, args.recursive)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if not pdf_paths:
        print("No PDF files found.", file=sys.stderr)
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)
    workers = args.workers if args.workers > 0 else auto_worker_count()

    failures = 0
    for pdf_path in pdf_paths:
        try:
            markdown_path, pages, image_count, active_workers = convert_pdf(
                pdf_path=pdf_path,
                output_dir=output_dir,
                max_pages=args.max_pages,
                min_width=args.min_image_width,
                min_height=args.min_image_height,
                min_area=args.min_image_area,
                image_dpi=args.image_dpi,
                workers=workers,
                chunk_size=args.chunk_size,
                keep_temp_pages=args.keep_temp_pages,
                overwrite=args.overwrite,
            )
            print(
                f"[ok] {pdf_path.name}: pages={pages}, images={image_count}, "
                f"workers={active_workers}, "
                f"markdown={markdown_path}"
            )
        except Exception as exc:  # pragma: no cover
            failures += 1
            print(f"[error] {pdf_path}: {exc}", file=sys.stderr)

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
