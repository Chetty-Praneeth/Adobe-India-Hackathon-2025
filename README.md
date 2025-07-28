# PDF Outline Extraction – Challenge Suite

This repository contains solutions to both **Challenge 1A** and **Challenge 1B**, focused on extracting structured outline and semantic data from collections of PDFs.

## Directory Structure

```
pdf-outline-extractor/
├── Challenge_1a/
│   ├── sample_dataset/
│   │   ├── pdfs/
│   │   ├── output/
│   │   └── schema/
│   ├── Dockerfile
│   ├── process_pdf.py
│   ├── ...
│   └── README.md
├── Challenge_1b/
│   ├── Collection 1/
│   ├── Collection 2/
│   ├── Collection 3/
│   ├── analyze_collection.py
│   ├── Dockerfile
│   └── README.md
├── run_all.sh
└── requirements.txt
```

## How to Run

Use Docker to build and run each challenge individually. You can also use the included `run_all.sh` script to process all Challenge 1B collections at once.

```bash
# Build and run Challenge 1A
cd Challenge_1a
docker build -t pdf-outline-1a .
docker run --rm -v "$PWD/sample_dataset:/app/sample_dataset" pdf-outline-1a

# Build and run Challenge 1B
cd ../Challenge_1b
docker build -t pdf-outline-1b .
docker run --rm -v "$PWD/Collection\ 1:/app/Collection\ 1" pdf-outline-1b

# Alternatively run all collections
bash run_all.sh
```

## Notes

- Ensure Docker is installed and running.
- Outputs will be written alongside input files for each challenge.
