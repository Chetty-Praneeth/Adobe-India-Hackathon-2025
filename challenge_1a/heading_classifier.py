def classify_headings(candidates):
    # Get unique font sizes sorted high to low
    sizes = sorted({block["font_size"] for block in candidates}, reverse=True)

    level_map = {}
    if len(sizes) >= 1:
        level_map[sizes[0]] = "H1"
    if len(sizes) >= 2:
        level_map[sizes[1]] = "H2"
    if len(sizes) >= 3:
        level_map[sizes[2]] = "H3"

    outline = []
    for block in candidates:
        size = block["font_size"]
        level = level_map.get(size, "H3")
        outline.append({
            "level": level,
            "text": block["text"],
            "page": block["page"]
        })

    return outline
