# AWS SageMaker PDF -> ML Dataset Prep

This repo converts large PDF docs into machine-learning-friendly assets:

- markdown text (`document.md`)
- extracted diagram/image files (`images/`)
- metadata manifest (`manifest.json`)

The markdown includes references to the extracted images so text and diagrams stay connected.

## Input PDFs

PDF source files are expected to stay local (for example on `~/Desktop`) and are not committed to this repository.

## Setup

```bash
./tools/setup_venv.sh
```

## Run on one PDF

```bash
python3 tools/pdf_to_markdown.py \
  --input /Users/alicopur/Desktop/sagemaker-dg-8318.pdf \
  --output-dir ml-output \
  --overwrite
```

If you used `./tools/setup_venv.sh`, run with:

```bash
.venv/bin/python3 tools/pdf_to_markdown.py \
  --input /Users/alicopur/Desktop/sagemaker-dg-8318.pdf \
  --output-dir ml-output \
  --overwrite
```

## Run on similar files in a folder

```bash
python3 tools/pdf_to_markdown.py \
  --input /Users/alicopur/Desktop \
  --pattern 'sagemaker-dg-*.pdf' \
  --recursive \
  --output-dir ml-output \
  --overwrite
```

## Optimized for MacBook Pro M1 Max (32GB)

Use the pre-tuned runner:

```bash
./tools/run_m1_max.sh
```

This uses:

- process-level parallelism (`--workers`, auto-capped at 8)
- balanced chunking (`--chunk-size 12`)
- tuned diagram filters to keep useful visual references
- repo-local output directory (`ml-output/`)

## Output Format

For each PDF `<name>.pdf`, the script writes:

- `ml-output/<name>/document.md`
- `ml-output/<name>/images/*`
- `ml-output/<name>/manifest.json`

## Notes

- This repository does not push PDF source files.
- Tune diagram extraction sensitivity with:
  - `--min-image-width`
  - `--min-image-height`
  - `--min-image-area`
