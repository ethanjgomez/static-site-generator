from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = list()
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split = old_node.text.split(delimiter)
        if len(split) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        split_res = list()
        for i, s in enumerate(split):
            if not s:
                continue
            if i % 2 == 0:
                split_res.append(TextNode(s, TextType.TEXT))
            else:
                split_res.append(TextNode(s, text_type))
        new_nodes.extend(split_res)
    return new_nodes