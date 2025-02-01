import re

def extract_markdown_images(text):
    """
    Extracts markdown image alt text and URLs.
    Args:
        text (str): The raw markdown text.
    Returns:
        List[Tuple[str, str]]: A list of tuples with alt text and URLs.
    """
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regex, text)
def extract_markdown_links(text):
    """
    Extracts markdown link text and URLs.
    Args:
        text (str): The raw markdown text.
    Returns:
        List[Tuple[str, str]]: A list of tuples with anchor text and URLs.
    """
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regex, text)

def markdown_to_blocks(markdown):
    """
    Splits a raw Markdown document into a list of block strings.

    - First splits on double newlines.
    - For each block, if any line (after stripping) starts with "*", the newlines between items are preserved.
    - Otherwise, all lines in the block are joined with a single space.
    - Each line is stripped of extra whitespace.

    Args:
        markdown (str): The raw Markdown text.

    Returns:
        list: A list of block strings.
    """
    # First split on double newlines
    raw_blocks = markdown.split("\n\n")
    blocks = []
    
    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue

        lines = block.split("\n")
        # Check if any line starts with "*" after stripping leading whitespace
        if any(line.lstrip().startswith("*") for line in lines):
            # Preserve newlines by stripping each line and rejoining with "\n"
            processed = "\n".join(line.strip() for line in lines)
        else:
            # Otherwise, join lines with a single space
            processed = " ".join(line.strip() for line in lines)
        
        blocks.append(processed)
    
    return blocks