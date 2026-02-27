# AWS SageMaker PDF -> ML Dataset Prep

This repo converts large PDF docs into machine-learning-friendly assets:

- markdown text (`document.md`)
- extracted diagram/image files (`images/`)
- metadata manifest (`manifest.json`)

The markdown includes references to the extracted images so text and diagrams stay connected.

## Included Sample PDF

- `pdfs/sagemaker-dg-8318.pdf` (tracked with Git LFS)

## Setup

```bash
python3 -m pip install -r requirements.txt
```

## Run on one PDF

```bash
python3 tools/pdf_to_markdown.py \
  --input /Users/alicopur/Desktop/sagemaker-dg-8318.pdf \
  --output-dir artifacts \
  --overwrite
```

## Run on similar files in a folder

```bash
python3 tools/pdf_to_markdown.py \
  --input /Users/alicopur/Desktop \
  --pattern 'sagemaker-dg-*.pdf' \
  --recursive \
  --output-dir artifacts \
  --overwrite
```

## Output Format

For each PDF `<name>.pdf`, the script writes:

- `artifacts/<name>/document.md`
- `artifacts/<name>/images/*`
- `artifacts/<name>/manifest.json`

## Notes

- Large PDFs in this repo are stored via Git LFS.
- Tune diagram extraction sensitivity with:
  - `--min-image-width`
  - `--min-image-height`
  - `--min-image-area`
