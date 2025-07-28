# PDF Outline Extractor – Challenge 1B

This project is the second part of a document understanding pipeline, where we go beyond just extracting structure and dive into **personalized, context-aware document summarization**. Designed for scenarios where a user (persona) is trying to achieve a specific task using a collection of PDFs, this solution ranks and extracts the most relevant sections and subsections — as if the system were tailored just for them.

---

## Approach

Challenge 1B takes our work from 1A and kicks it up a notch!  
Here, we don’t just extract structure — we **personalize** the experience. The goal? Mimic how a real user with a specific persona and task would *think*, *search*, and *extract insights* from complex PDFs.

###  1. Persona-Driven Intelligence

We begin by parsing a JSON input that defines:

- The **persona** (who the user is)
- The **job to be done** (what they want to achieve)
- A list of relevant PDF documents

These details aren't just metadata — they directly influence how we score content for relevance.

### 2. Power of 1A — Structural Reuse

Rather than reinventing the wheel, we build on the robust structural tools from Challenge 1A:

- `extract_headings_from_pdf` to detect and extract section titles
- `extract_text_blocks` to capture paragraph-level data for fine-grained analysis

These help break down the PDFs into logical units for intelligent filtering.

### 3. Relevance Scoring — But Smart

We tokenize both the **persona role** and **task description** into keywords.

Each heading and paragraph block is then scored based on:

- Presence of those keywords (case-insensitive)
- Degree of overlap (i.e., higher keyword hits = more relevant)

 If a heading has ≥ 1 hit → it's marked as a relevant **section**  
 If a paragraph/block has ≥ 2 hits → it's a refined **subsection**

### 4. Ranking for Clarity

All relevant sections and subsections are:

- **Ranked by importance** (number of keyword hits)
- **Filtered to top 10** from each category to ensure concise yet rich output

This creates a final JSON output that reads like a well-researched summary crafted *for the persona*.

---

##  Docker Instructions

###  Build the Docker Image

```bash
docker build -f challenge_1b/Dockerfile -t pdf-outline-1b .
```

###  Run on a Specific Collection

```bash
docker run --rm -v "$PWD/Challenge_1b/Collection 1:/app/Challenge_1b/Collection 1" pdf-outline-1b python Challenge_1b/analyze_collection.py "Challenge_1b/Collection 1"

```

###  Run All Collections Using `run_all.sh`

To analyze multiple collections in a batch mode:

```bash
bash run_all.sh
```

Make sure `run_all.sh` contains the correct loop and paths pointing to all your collection folders.

---

##  Output

Each collection will generate a `challenge1b_output.json` file with the following fields:

- `metadata`: persona, task, input files, timestamp
- `extracted_sections`: top 10 relevant headings
- `subsection_analysis`: top 10 refined body text sections

---

##  Dependencies

Install via Docker automatically. If running locally:

```bash
pip install -r requirements.txt
```

---