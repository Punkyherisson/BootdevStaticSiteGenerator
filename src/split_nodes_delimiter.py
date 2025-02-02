from copy import deepcopy  # standard library import first
from textnode import TextNode, TextType  # local imports
from markdown_extractors import extract_markdown_images, extract_markdown_links
from enum import Enum

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    print(f"\nProcessing delimiter: {delimiter}")
    new_nodes = []
    for old_node in old_nodes:
        print(f"Processing node: {old_node.text}")
        print(f"Node type: {old_node.text_type}")
        
        if old_node.text_type != TextType.TEXT:
            print("Skipping non-TEXT node")
            new_nodes.append(old_node)
            continue
            
        text = old_node.text
        start = text.find(delimiter)
        print(f"Start position: {start}")
        
        if start == -1:
            print("No delimiter found")
            new_nodes.append(old_node)
            continue
            
        end = text.find(delimiter, start + len(delimiter))
        print(f"End position: {end}")
        
        if end == -1:
            print("No closing delimiter found")
            new_nodes.append(old_node)
            continue
            
        before = text[:start]
        between = text[start + len(delimiter):end]
        after = text[end + len(delimiter):]
        print(f"Before: '{before}'")
        print(f"Between: '{between}'")
        print(f"After: '{after}'")
        # Add the parts as nodes
        if before:
            new_nodes.append(TextNode(before, TextType.TEXT))
        if between:
            new_nodes.append(TextNode(between, text_type))
        if after:
            remaining_node = TextNode(after, TextType.TEXT)
            # Process the remaining text for more delimiters
            new_nodes.extend(split_nodes_delimiter([remaining_node], delimiter, text_type))
                
    return new_nodes

def split_nodes_image(old_nodes):
    """
    Splits TextNode objects based on Markdown image syntax.

    Args:
        old_nodes (list): A list of TextNode objects.
    Returns:
        list: A new list of TextNode objects, split by images.
    """

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Add non-text nodes as-is
            new_nodes.append(node)
            continue

        # Extract images from the text
        images = extract_markdown_images(node.text)
        text = node.text

        if not images:
            # No images, keep the original node
            new_nodes.append(node)
            continue

        # Process text and images
        for alt, url in images:
            # Split the text into sections based on the current image
            sections = text.split(f"![{alt}]({url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            text = sections[1] if len(sections) > 1 else ""

        # Add remaining text, if any
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    """
    Splits TextNode objects based on Markdown link syntax.

    Args:
        old_nodes (list): A list of TextNode objects.
    Returns:
        list: A new list of TextNode objects, split by links.
    """

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Add non-text nodes as-is
            new_nodes.append(node)
            continue

        # Extract links from the text
        links = extract_markdown_links(node.text)
        text = node.text

        if not links:
            # No links, keep the original node
            new_nodes.append(node)
            continue

        # Process text and links
        for anchor, url in links:
            # Split the text into sections based on the current link
            sections = text.split(f"[{anchor}]({url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(anchor, TextType.LINK, url))
            text = sections[1] if len(sections) > 1 else ""

        # Add remaining text, if any
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes