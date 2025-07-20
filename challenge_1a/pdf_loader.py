import fitz  

def extract_text_blocks(pdf_path):
    doc = fitz.open(pdf_path)
    blocks = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks_data = page.get_text("dict")["blocks"]

        for block in blocks_data:
            if "lines" not in block:
                continue

            for line in block["lines"]:
                line_text = ""
                max_font_size = 0
                bold = False
                x, y = 0, 0

                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text:
                        continue

                    line_text += text + " "
                    font = span["font"]
                    size = span["size"]

                    # Font weight check
                    if "Bold" in font or "bold" in font:
                        bold = True

                    max_font_size = max(max_font_size, size)
                    x, y = span["origin"]

                line_text = line_text.strip()

                if line_text:  # Skip empty lines
                    blocks.append({
                        "text": line_text,
                        "font_size": round(max_font_size, 2),
                        "bold": bold,
                        "x": round(x, 2),
                        "y": round(y, 2),
                        "page": page_num + 1  # 1-based indexing
                    })

    doc.close()
    return blocks

if __name__ == "__main__":
    import sys
    from pprint import pprint

    pdf_file = sys.argv[1]  # e.g., sample.pdf
    result = extract_text_blocks(pdf_file)
    pprint(result[:10])