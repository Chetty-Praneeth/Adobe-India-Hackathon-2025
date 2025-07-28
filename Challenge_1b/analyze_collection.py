import os
import json
import argparse
import datetime
import sys
from pathlib import Path
sys.path.append(os.path.dirname(__file__))

# Add Challenge 1A folder to import modules
sys.path.append(str(Path(__file__).resolve().parents[1] / "Challenge_1a"))
from heading_extractor import extract_headings_from_pdf
from pdf_loader import extract_text_blocks

def compute_relevance(text, keywords):
    text_lower = text.lower()
    return sum(1 for word in keywords if word in text_lower)

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

        headings = extract_headings_from_pdf(file_path)
        blocks = extract_text_blocks(file_path)

        # Find relevant headings
        for heading in headings:
            score = compute_relevance(heading["text"], keywords)
            if score >= 1:
                extracted_sections.append({
                    "document": filename,
                    "section_title": heading["text"],
                    "importance_rank": score,
                    "page_number": heading["page"]
                })

        # Find relevant body paragraphs
        for block in blocks:
            score = compute_relevance(block["text"], keywords)
            if score >= 2:
                subsection_analysis.append({
                    "document": filename,
                    "refined_text": block["text"].strip(),
                    "page_number": block["page"]
                })

    # Sort and limit to top 10
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
    parser = argparse.ArgumentParser()
    parser.add_argument("collection_path", type=str)
    args = parser.parse_args()
    analyze_collection(args.collection_path)
