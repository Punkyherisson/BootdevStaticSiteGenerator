from htmlnode import HTMLNode, ParentNode, LeafNode  # Add ParentNode and LeafNode
from text_parser import text_to_textnodes  # Converts inline Markdown to text nodes
from markdown_blocks import markdown_to_blocks, block_to_block_type  # Changed from extract_markdown


def text_to_children(text):
    """
    Converts inline markdown text into a list of HTMLNode objects.
    """
    text_nodes = text_to_textnodes(text)
    return [node.to_html_node() for node in text_nodes]  # Changed from to_node()

def markdown_to_html_node(markdown):
    """
    Converts a full markdown document into a single parent HTMLNode.
    
    Args:
        markdown (str): The raw markdown document.
    
    Returns:
        HTMLNode: The root HTMLNode representing the entire document.
    """
    blocks = markdown_to_blocks(markdown)
    children = []  # Create a list to store children

    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == "heading":
            level = block.count("#", 0, block.index(" "))
            content = block[level + 1:].strip()
            children.append(ParentNode(tag=f"h{level}", children=text_to_children(content)))

        elif block_type == "code":
            content = block.strip("```").strip()
            children.append(ParentNode(tag="pre", children=[
                ParentNode(tag="code", children=[LeafNode(tag=None, value=content)])
            ]))

        elif block_type == "quote":
            quote_text = "\n".join(line[1:].strip() for line in block.split("\n"))
            children.append(ParentNode(tag="blockquote", children=text_to_children(quote_text)))
            
        elif block_type == "unordered_list":
            items = [line[2:].strip() for line in block.split("\n")]
            list_items = [ParentNode(tag="li", children=text_to_children(item)) for item in items]
            children.append(ParentNode(tag="ul", children=list_items))

        elif block_type == "ordered_list":
            items = [line[line.index(" ") + 1:].strip() for line in block.split("\n")]
            list_items = [ParentNode(tag="li", children=text_to_children(item)) for item in items]
            children.append(ParentNode(tag="ol", children=list_items))

        else:  # Default to paragraph
            children.append(ParentNode(tag="p", children=text_to_children(block)))

    # Create the root node with all children
    return ParentNode(tag="div", children=children)