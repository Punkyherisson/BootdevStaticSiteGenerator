def split_nodes_image(old_nodes):
    """
    Splits TextNode objects based on Markdown image syntax.

    Args:
        old_nodes (list): A list of TextNode objects.
    Returns:
        list: A new list of TextNode objects, split by images.
    """
    from copy import deepcopy

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
    from copy import deepcopy

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