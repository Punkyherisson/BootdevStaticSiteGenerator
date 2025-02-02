from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link    

def text_to_textnodes(text):
    """
    Converts a raw markdown-flavored string into a list of TextNode objects.

    Args:
        text (str): Raw markdown-flavored text.

    Returns:
        list: A list of TextNode objects.
    """
    # Start with a single TextNode containing the raw text
    nodes = [TextNode(text, TextType.TEXT)]

    # Apply each splitting function in the correct order
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

    # Return the fully processed list of nodes
    return nodes    