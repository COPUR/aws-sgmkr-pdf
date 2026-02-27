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
import json
import sys
from pathlib import Path
from typing import Any

try:
    import fitz  # type: ignore
except ImportError:  # pragma: no cover
    fitz = None


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
        default="artifacts",
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


def save_image_block(
    doc: Any,
    page: Any,
    block: dict[str, Any],
    destination_base: Path,
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
    pix = page.get_pixmap(clip=rect, alpha=False, dpi=200)
    image_path = destination_base.with_suffix(".png")
    pix.save(str(image_path))
    return image_path


def convert_pdf(
    pdf_path: Path,
    output_dir: Path,
    max_pages: int,
    min_width: float,
    min_height: float,
    min_area: float,
    overwrite: bool,
) -> tuple[Path, int, int]:
    doc_name = pdf_path.stem
    doc_out_dir = output_dir / doc_name
    images_dir = doc_out_dir / "images"
    markdown_path = doc_out_dir / "document.md"
    manifest_path = doc_out_dir / "manifest.json"

    if doc_out_dir.exists() and not overwrite:
        raise FileExistsError(
            f"Output already exists: {doc_out_dir}. Use --overwrite to replace it."
        )
    doc_out_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(pdf_path))
    pages_to_process = doc.page_count if max_pages <= 0 else min(doc.page_count, max_pages)

    markdown_lines: list[str] = [f"# {pdf_path.name}", ""]
    manifest: dict[str, Any] = {
        "source_pdf": str(pdf_path.resolve()),
        "page_count": pages_to_process,
        "images": [],
    }
    extracted_image_count = 0

    for page_index in range(pages_to_process):
        page_number = page_index + 1
        page = doc.load_page(page_index)
        page_dict = page.get_text("dict")
        blocks = page_dict.get("blocks", [])
        blocks.sort(key=lambda b: (b.get("bbox", [0, 0])[1], b.get("bbox", [0, 0])[0]))

        markdown_lines.append(f"## Page {page_number}")
        markdown_lines.append("")

        page_image_index = 0
        for block in blocks:
            block_type = block.get("type")
            if block_type == 0:
                text = safe_text_from_block(block)
                if text:
                    markdown_lines.append(text)
                    markdown_lines.append("")
                continue

            if block_type != 1:
                continue

            bbox = block.get("bbox", [0, 0, 0, 0])
            width = float(bbox[2] - bbox[0])
            height = float(bbox[3] - bbox[1])
            area = width * height

            if width < min_width or height < min_height or area < min_area:
                continue

            page_image_index += 1
            extracted_image_count += 1
            image_base = images_dir / f"page-{page_number:04d}-img-{page_image_index:02d}"
            image_path = save_image_block(doc, page, block, image_base)
            if image_path is None:
                extracted_image_count -= 1
                continue

            rel_image_path = image_path.relative_to(doc_out_dir).as_posix()
            markdown_lines.append(
                f"![Page {page_number} Diagram {page_image_index}]({rel_image_path})"
            )
            markdown_lines.append("")

            manifest["images"].append(
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

    markdown_path.write_text("\n".join(markdown_lines).strip() + "\n", encoding="utf-8")
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return markdown_path, pages_to_process, extracted_image_count


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

    failures = 0
    for pdf_path in pdf_paths:
        try:
            markdown_path, pages, image_count = convert_pdf(
                pdf_path=pdf_path,
                output_dir=output_dir,
                max_pages=args.max_pages,
                min_width=args.min_image_width,
                min_height=args.min_image_height,
                min_area=args.min_image_area,
                overwrite=args.overwrite,
            )
            print(
                f"[ok] {pdf_path.name}: pages={pages}, images={image_count}, "
                f"markdown={markdown_path}"
            )
        except Exception as exc:  # pragma: no cover
            failures += 1
            print(f"[error] {pdf_path}: {exc}", file=sys.stderr)

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
