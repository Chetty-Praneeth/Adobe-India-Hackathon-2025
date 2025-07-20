import json
import os

def write_json(output_path, title, outline):
    result = {
        "title": title,
        "outline": outline
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    sample_title = "Understanding AI"
    sample_outline = [
        {"level": "H1", "text": "Introduction", "page": 1},
        {"level": "H2", "text": "History", "page": 2}
    ]
    write_json("output/sample.json", sample_title, sample_outline)
