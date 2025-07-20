# Challenge 1A

This solution is for **Challenge 1A** of the Adobe India Hackathon 2025 – *Connecting the Dots*.  
It extracts a structured outline (document title and hierarchical headings) from PDF documents while adhering to all technical constraints defined in the challenge.

---

## Approach

Our solution uses a lightweight, modular pipeline that mimics human document reading by leveraging font size, boldness, and position to extract structure from raw PDFs.

### 1. PDF Parsing

- We use `PyMuPDF` (`fitz`) to extract all text blocks along with their positional, font, and formatting metadata.
- This allows us to interpret layout, heading structure, and visual hierarchy.

### 2. Title Detection

- We analyze the upper portion of the first page.
- Each block is scored using a weighted function based on:
  - Font size
  - Boldness
  - Vertical position
- The highest-scoring block is selected as the **document title**.

### 3. Heading Classification

- Each text block is converted into a feature vector based on:
  - Font size
  - Bold weight
  - Distance from the top
  - Relative indentation
- A rule-based classifier predicts the heading level (`H1`, `H2`, or `H3`).
- This logic avoids the need for heavy ML models, staying within the 200MB limit.

### 4. Structured Outline Generation

- Heading blocks are grouped by level and assigned page numbers.
- The result is a clean, hierarchical `outline` array matching the provided JSON schema.

---

## 📦 Models and Libraries Used

| Library           | Usage                                |
|-------------------|---------------------------------------|
| `PyMuPDF (fitz)`  | PDF parsing with layout + style info |
| `os`, `json`, `re`| File and data formatting              |

> No large models are used. The total dependency + codebase is under 200MB.  
> The solution works **offline**, runs on **CPU**, and supports **linux/amd64** as required.

---

## Input Format

- PDFs are placed inside the `sample_dataset/pdfs/` directory.
- This directory is mounted as read-only into the Docker container.

---

## Output Format

Each PDF generates a JSON file in the following format:

    ```json
    {
    "title": "Detected Title",
    "outline": [
        {
        "level": "H1" | "H2" | "H3",
        "text": "Heading Text",
        "page": PageNumber
        }
    ]
    }
--- 

Output is saved to sample_dataset/output/ and validated against output_schema.json.
