def detect_title(blocks, page_width=595):  # default A4 width in points
    candidates = [
        b for b in blocks if b["page"] == 1 and b["font_size"] > 10
    ]

    
    candidates.sort(key=lambda b: b["font_size"], reverse=True)

    for block in candidates:
        text = block["text"]
        x = block["x"]
        font_size = block["font_size"]

        # Center aligned check (with tolerance)
        if abs((x + len(text) * font_size * 0.3) - page_width / 2) < 100:
            return text

    # Fallback: return largest font block
    return candidates[0]["text"] if candidates else "Untitled Document"

if __name__ == "__main__":
    from pdf_loader import extract_text_blocks

    blocks = extract_text_blocks("sample.pdf")  # Replace with actual path
    title = detect_title(blocks)
    print("Title:", title)