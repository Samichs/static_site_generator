from textnode import TextType, TextNode

delimiter_to_type_map = {"**": TextType.BOLD, "*": TextType.ITALIC, "`": TextType.CODE}

"""
Handle nested delimiters by controlling order of precedence 
(e.g. italics before bold, because '*' is contained within '**'
"""


def split_nodes_delimiter(old_nodes, delimiter):
    if delimiter not in delimiter_to_type_map:
        raise ValueError(f"delimiter {delimiter} does not map to a known TextType")

    result = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL.value:
            result.append(node)
            continue

        split_node_text = node.text.split(delimiter)
        if len(split_node_text) == 1:
            result.append(node)
            continue
        if len(split_node_text) != 3:
            raise Exception("could not find block of text inside delimiters")

        result.append(TextNode(split_node_text[0], TextType.NORMAL))
        result.append(TextNode(split_node_text[1], delimiter_to_type_map[delimiter]))
        result.append(TextNode(split_node_text[2], TextType.NORMAL))

    return result
