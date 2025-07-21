def extract_heading_candidates(blocks):
    candidates = []

    for block in blocks:
        text = block["text"]
        font_size = block["font_size"]
        bold = block["bold"]

        # Basic filters
        if len(text.split()) > 12:
            continue  

        if font_size < 10:
            continue  

        if not bold and not text.isupper():
            continue  

        candidates.append(block)

    return candidates

if __name__ == "__main__":
    from pdf_loader import extract_text_blocks
    blocks = extract_text_blocks("sample.pdf")

    from heading_extractor import extract_heading_candidates
    headings = extract_heading_candidates(blocks)

    for h in headings:
        print(f"{h['text']} (Font: {h['font_size']}, Page: {h['page']})")

from pdf_loader import extract_text_blocks

def extract_headings_from_pdf(pdf_path):
    blocks = extract_text_blocks(pdf_path)
    heading_candidates = extract_heading_candidates(blocks)
    return heading_candidates