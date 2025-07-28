# Challenge 1A 

This solution extracts a structured outline from PDFs by detecting headings and organizing them into a hierarchical JSON format. It supports batch processing of documents and is robust against varying document formats.

---

##  Approach

1. **PDF Parsing:**  
   PDFs from the `sample_dataset/pdfs/` folder are parsed using `PyMuPDF` (`fitz`) to extract text blocks along with their metadata (like font size, position, etc).

2. **Heading Detection:**  
   - `title_detector.py` identifies potential heading candidates based on formatting features like font size and weight.
   - `heading_classifier.py` uses heuristic logic to classify text blocks as headings.

3. **Heading Hierarchy Construction:**  
   - `heading_extractor.py` builds the heading tree (H1, H2, H3...) using indentation levels and relative font sizes.
   - Each heading is mapped to its corresponding page number.

4. **JSON Generation:**  
   - `json_writer.py` generates structured JSON output according to the schema defined in `sample_dataset/schema/`.
   - Output is saved to `sample_dataset/output/` with a filename corresponding to the PDF.

---

##  Libraries Used

- `PyMuPDF` (`fitz`) – for text extraction from PDFs
- `json` – to serialize extracted data into JSON format
- `os`, `argparse`, `pathlib` – for file handling and scripting

---
##  How to Run

###  Manual Execution

```bash
# Install dependencies
pip install -r requirements.txt

# Run processing
python process_pdf.py sample_dataset/pdfs/sample.pdf
```

> Output will be stored in `sample_dataset/output/sample.json`.

###  Docker Execution

```bash
# Build the image
docker build -t pdf-outline-1a .

# Run the container
docker run --rm -v "$PWD/sample_dataset:/app/sample_dataset" pdf-outline-1a
```

---

##  Output Format (Sample)

```json
{
  "title": "Sample PDF Title",
  "outline": [
    {
      "level": "H1",
      "text": "Introduction",
      "page": 1
    },
    {
      "level": "H2",
      "text": "Motivation",
      "page": 2
    }
  ]
}
```

---

## Notes

- Ensure your PDFs are placed in `sample_dataset/pdfs/`
- JSON output for each processed PDF will be placed in `sample_dataset/output/`
- You can modify heading classification logic in `heading_classifier.py` if your dataset requires special handling

---
