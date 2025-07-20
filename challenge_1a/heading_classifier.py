def classify_headings(candidates):
    sizes = sorted({b["font_size"] for b in candidates}, reverse=True)

    # Mapping font sizes to levels
    level_map = {}
    if len(sizes) >= 1:
        level_map[sizes[0]] = "H1"
    if len(sizes) >= 2:
        level_map[sizes[1]] = "H2"
    if len(sizes) >= 3:
        level_map[sizes[2]] = "H3"

    # Assign levels
    outline = []
    for block in candidates:
        size = block["font_size"]
        level = level_map.get(size)
        if level:
            outline.append({
                "level": level,
                "text": block["text"],
                "page": block["page"]
            })

    return outline

if __name__ == "__main__":
    from pdf_loader import extract_text_blocks
    from title_detector import detect_title
    from heading_extractor import extract_heading_candidates

    blocks = extract_text_blocks("sample.pdf")
    candidates = extract_heading_candidates(blocks)

    from heading_classifier import classify_headings
    structured_outline = classify_headings(candidates)

    print(structured_outline)
