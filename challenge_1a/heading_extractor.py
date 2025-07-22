# heading_extractor.py

def extract_heading_candidates(blocks):
    candidates = []

    for block in blocks:
        text = block["text"]
        font_size = block["font_size"]
        bold = block["bold"]

        # Filter based on visual cues
        if len(text.strip()) == 0 or len(text.split()) > 12:
            continue  # too long or empty

        if font_size < 10:
            continue  # probably body text

        if not bold and not text.isupper():
            continue  # headings tend to be bold or uppercase

        candidates.append(block)

    return candidates


def extract_headings_from_pdf(pdf_path):
    from pdf_loader import extract_text_blocks
    from heading_classifier import classify_headings

    blocks = extract_text_blocks(pdf_path)
    candidates = extract_heading_candidates(blocks)
    headings = classify_headings(candidates)

    return headings
