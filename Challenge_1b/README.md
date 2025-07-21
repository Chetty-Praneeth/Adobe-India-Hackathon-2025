# Challenge 1B

This solution is for **Challenge 1B** of the Adobe India Hackathon 2025 – *Connecting the Dots*.  
It performs persona-driven analysis by reviewing multiple PDFs and extracting sections most relevant to a specific user and their task.

---

## Approach

Our solution builds on Challenge 1A’s structural analysis by introducing a relevance-aware pipeline that mimics how a user would navigate large documents to find meaningful content tailored to their needs.

### 1. Input Parsing

- We load a JSON file that includes:
  - The user persona
  - The job-to-be-done
  - A list of PDF filenames
- The corresponding PDFs are loaded from the local folder.

### 2. Outline and Block Extraction

- We reuse `extract_headings_from_pdf` and `extract_text_blocks` from Challenge 1A:
  - Headings help us identify potential section titles.
  - Text blocks are used for deeper semantic scoring.

### 3. Keyword-Based Relevance Scoring

- We extract keywords from both the persona and job descriptions.
- Each heading and block of text is scored based on keyword matches:
  - Sections with a score ≥ 1 are selected.
  - Sub-sections with a score ≥ 2 are considered refined content.

### 4. Filtering and Ranking

- All matched sections and sub-sections are ranked by importance score.
- The top 10 results from both categories are returned in the final output.

---

## Models and Libraries Used

| Library             | Usage                                   |
|---------------------|------------------------------------------|
| `PyMuPDF (fitz)`    | PDF parsing with layout + style info     |
| `os`, `json`, `datetime` | File and data formatting          |
| `argparse`, `sys.path` | CLI and Challenge 1A module import   |

> No machine learning models are used. The total codebase + dependencies remain well below the 1GB limit.  
> The solution runs **offline**, on **CPU**, and supports **linux/amd64** as required.

---

## Input Format

- PDFs are placed inside the `PDFs/` subfolder in each collection directory.
- Each collection also contains a JSON file that specifies:
  - The persona (e.g., Travel Planner)
  - The job to be done (e.g., Plan a 4-day trip)
  - The list of associated PDF files.

The input JSON file must follow this structure:

    ```json
    {
      "persona": {
        "role": "Persona Role"
      },
      "job_to_be_done": {
        "task": "Job description or task"
      },
      "documents": [
        { "filename": "filename1.pdf" },
        { "filename": "filename2.pdf" }
      ]
    }

---

## Output Format

Each run generates a JSON file in the following format:

    ```json
    {
      "metadata": {
        "input_documents": ["filename1.pdf", "filename2.pdf"],
        "persona": "Persona Role",
        "job_to_be_done": "Job description or task",
        "processing_timestamp": "YYYY-MM-DDTHH:MM:SS"
      },
      "extracted_sections": [
        {
          "document": "filename.pdf",
          "section_title": "Section Heading Text",
          "importance_rank": Score,
          "page_number": Page
        }
      ],
      "subsection_analysis": [
        {
          "document": "filename.pdf",
          "refined_text": "Relevant sub-section text",
          "page_number": Page
        }
      ]
    }

---

Output is saved in the same directory as the input and can be validated against an output schema if provided.