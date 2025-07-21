import os
import json
import argparse
import datetime
import sys
from pathlib import Path
from pathlib import Path

# Add the parent directory to sys.path to access challenge_1a modules
sys.path.append(str(Path(__file__).resolve().parents[1] / "challenge_1a"))
from heading_extractor import extract_headings_from_pdf  # from Challenge 1A
from pdf_loader import extract_text_blocks              # from Challenge 1A

# Simple keyword matching for relevance scoring
def compute_relevance(text, keywords):
    score = 0
    for word in keywords:
        if word.lower() in text.lower():
            score += 1
    return score

def analyze_collection(collection_path):
    input_path = Path(collection_path) / "challenge1b_input.json"
    output_path = Path(collection_path) / "challenge1b_output.json"

    with open(input_path, "r") as f:
        input_data = json.load(f)

    documents = input_data["documents"]
    persona = input_data["persona"]["role"]
    task = input_data["job_to_be_done"]["task"]
    keywords = task.lower().split() + persona.lower().split()

    extracted_sections = []
    subsection_analysis = []

    for doc in documents:
        filename = doc["filename"]
        file_path = Path(collection_path) / "PDFs" / filename

        # Extract headings using Challenge 1A tools
        headings = extract_headings_from_pdf(file_path)
        blocks = extract_text_blocks(file_path)

        for heading in headings:
            text = heading["text"]
            score = compute_relevance(text, keywords)
            if score >= 1:
                extracted_sections.append({
                    "document": filename,
                    "section_title": text,
                    "importance_rank": score,
                    "page_number": heading["page"]
                })

        # Now grab page-wise refined content
        for block in blocks:
            text = block["text"]
            page = block["page"]
            score = compute_relevance(text, keywords)
            if score >= 2:  # more strict for refined content
                subsection_analysis.append({
                    "document": filename,
                    "refined_text": text.strip(),
                    "page_number": page
                })

    # Sort based on importance score
    extracted_sections.sort(key=lambda x: -x["importance_rank"])

    output_data = {
        "metadata": {
            "input_documents": [doc["filename"] for doc in documents],
            "persona": persona,
            "job_to_be_done": task,
            "processing_timestamp": datetime.datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections[:10],
        "subsection_analysis": subsection_analysis[:10]
    }

    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)

    print(f"Analysis complete: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze PDF collection for Challenge 1B")
    parser.add_argument("collection_path", type=str, help="Path to the collection folder")
    args = parser.parse_args()

    analyze_collection(args.collection_path)
