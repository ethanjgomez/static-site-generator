def markdown_to_blocks(markdown):
    res = list()
    rel_markdown = [t.strip() for t in markdown.split("\n\n")]
    for txt in [t for t in rel_markdown if t]:
        res.append(txt)
    return res

