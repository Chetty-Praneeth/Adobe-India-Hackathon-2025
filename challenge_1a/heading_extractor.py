def extract_heading_candidates(blocks):
    candidates = []

    for block in blocks:
        text = block["text"]
        font_size = block["font_size"]
        bold = block["bold"]

        # Basic filters
        if len(text.split()) > 12:
            continue  # too long to be a heading

        if font_size < 10:
            continue  # probably body text

        if not bold and not text.isupper():
            continue  # we prefer bold or uppercase headings

        candidates.append(block)

    return candidates

if __name__ == "__main__":
    from pdf_loader import extract_text_blocks
    blocks = extract_text_blocks("sample.pdf")

    from heading_extractor import extract_heading_candidates
    headings = extract_heading_candidates(blocks)

    for h in headings:
        print(f"{h['text']} (Font: {h['font_size']}, Page: {h['page']})")
