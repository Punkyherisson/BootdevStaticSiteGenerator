from htmlnode import HTMLNode  # Assuming you have an HTMLNode class
from text_parser import text_to_textnodes  # Converts inline Markdown to text nodes
from extract_markdown import markdown_to_blocks, block_to_block_type  # Block processing functions

def text_to_children(text):
    """
    Converts inline markdown text into a list of HTMLNode objects.
    """
    text_nodes = text_to_textnodes(text)
    return [node.to_html_node() for node in text_nodes]  # Convert each TextNode to HTMLNode

def markdown_to_html_node(markdown):
    """
    Converts a full markdown document into a single parent HTMLNode.
    
    Args:
        markdown (str): The raw markdown document.
    
    Returns:
        HTMLNode: The root HTMLNode representing the entire document.
    """
    blocks = markdown_to_blocks(markdown)
    print("Blocks:", blocks)  # Debug the blocks
    print("Input markdown:", markdown)
    print("Blocks created:", blocks)

    parent_node = HTMLNode(tag="div", children=[])

    for block in blocks:
        block_type = block_to_block_type(block)
        print(f"Block: '{block}'")
        print(f"Block type: {block_type}")

        if block_type == "heading":
            level = block.count("#", 0, block.index(" "))  # Get the heading level
            content = block[level + 1:].strip()  # Remove heading marker
            parent_node.children.append(HTMLNode(tag=f"h{level}", children=text_to_children(content)))

        elif block_type == "code":
            content = block.strip("```").strip()
            parent_node.children.append(HTMLNode(tag="pre", children=[HTMLNode(tag="code", children=[content])]))

        elif block_type == "quote":
            quote_text = "\n".join(line[1:].strip() for line in block.split("\n"))  # Remove leading '>'
            parent_node.children.append(HTMLNode(tag="blockquote", children=text_to_children(quote_text)))

        elif block_type == "unordered_list":
            items = [line[2:].strip() for line in block.split("\n")]  # Remove leading "* " or "- "
            list_items = [HTMLNode(tag="li", children=text_to_children(item)) for item in items]
            parent_node.children.append(HTMLNode(tag="ul", children=list_items))

        elif block_type == "ordered_list":
            items = [line[line.index(" ") + 1:].strip() for line in block.split("\n")]  # Extract list content
            list_items = [HTMLNode(tag="li", children=text_to_children(item)) for item in items]
            parent_node.children.append(HTMLNode(tag="ol", children=list_items))

        else:  # Default to paragraph
            parent_node.children.append(HTMLNode(tag="p", children=text_to_children(block)))
    print("Number of children created:", len(parent_node.children))
    print("Children:", parent_node.children)       

    return parent_node