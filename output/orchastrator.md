# Output Orchastrator

This document orchestrates ingestion and validation for extracted markdown and diagrams under `output/`.

## Inventory Summary

- Documents: **9**
- Total pages: **8326**
- Total diagram images: **629**
- Output footprint: **~260 MB**

## Dataset Inventory

| Source | Pages | Images | Markdown Image Refs | Status | Workers | Chunk Size | DPI |
|---|---:|---:|---:|---|---:|---:|---:|
| `sagemaker-dg-1000` | 1000 | 73 | 73 | OK | 8 | 12 | 170 |
| `sagemaker-dg-2000` | 1001 | 96 | 96 | OK | 8 | 12 | 170 |
| `sagemaker-dg-3000` | 1001 | 57 | 57 | OK | 8 | 12 | 170 |
| `sagemaker-dg-4000` | 1001 | 118 | 118 | OK | 8 | 12 | 170 |
| `sagemaker-dg-5000` | 1001 | 101 | 101 | OK | 8 | 12 | 170 |
| `sagemaker-dg-6000` | 1001 | 62 | 62 | OK | 8 | 12 | 170 |
| `sagemaker-dg-7000` | 1001 | 83 | 83 | OK | 8 | 12 | 170 |
| `sagemaker-dg-8000` | 1001 | 28 | 28 | OK | 8 | 12 | 170 |
| `sagemaker-dg-8318` | 319 | 11 | 11 | OK | 8 | 12 | 170 |

## Canonical Paths

- `output/sagemaker-dg-*/document.md`: extracted text with inline image references
- `output/sagemaker-dg-*/manifest.json`: extraction metadata and image index
- `output/sagemaker-dg-*/images/`: per-document diagram image files
- `output/pictures/<source>/`: exposed consolidated pictures per source PDF

## Orchestration Flow

1. Validate integrity for each source package:
   - `document.md` exists
   - `manifest.json` exists
   - `images/` exists
   - `image count == markdown image refs`
2. Build text chunks by splitting `document.md` on `## Page N`.
3. Attach metadata to each chunk:
   - `source`
   - `page`
   - `image_paths`
   - `manifest_path`
4. Build diagram dataset from `output/pictures/<source>/`.
5. Export machine-learning artifacts:
   - `output/datasets/text_chunks.jsonl`
   - `output/datasets/diagram_index.jsonl`
   - `output/datasets/doc_registry.json`
6. Index for retrieval (RAG) using key: `source + page`.

## Validation Command

```bash
cd /private/tmp/aws-sgmkr-ml
.venv/bin/python3 - <<'PY'
from pathlib import Path
base = Path("output")
for d in sorted(base.glob("sagemaker-dg-*")):
    manifest = d / "manifest.json"
    markdown = d / "document.md"
    images = d / "images"
    if not (manifest.exists() and markdown.exists() and images.exists()):
        print(f"{d.name}: missing required files")
        continue
    refs = markdown.read_text(encoding="utf-8", errors="ignore").count("![Page")
    img_count = len(list(images.glob("*")))
    print(f"{d.name}: images={img_count}, refs={refs}, ok={img_count == refs}")
PY
```
