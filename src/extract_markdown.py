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
def markdown_to_blocks(markdown):
    blocks = []
    current_block = []
    
    for line in markdown.split('\n'):
        line = line.strip()
        
        # Start a new block if we see a heading
        if line.startswith('#'):
            if current_block:  # Save the previous block if it exists
                blocks.append('\n'.join(current_block))
            current_block = [line]  # Start new block with heading
            continue  # Skip to next line
            
        # Empty line means end of current block
        if line == '':
            if current_block:  # Save the previous block if it exists
                blocks.append('\n'.join(current_block))
                current_block = []
        # Non-empty line that's not a heading
        elif not line.startswith('#'):
            if current_block and current_block[0].startswith('#'):
                # If we had a heading, start a new block
                blocks.append('\n'.join(current_block))
                current_block = [line]
            else:
                current_block.append(line)
    
    # Don't forget the last block
    if current_block:
        blocks.append('\n'.join(current_block))
    
    return [block for block in blocks if block]

def block_to_block_type(block):
    """
    Determines the type of a given markdown block.

    Args:
        block (str): A stripped block of markdown text.

    Returns:
        str: The type of the block (e.g., "heading", "code", "quote", "unordered_list", "ordered_list", "paragraph").
    """

    # Check for heading (1-6 # characters followed by a space)
    if re.match(r"^#{1,6} ", block):
        return "heading"

    # Check for code block (starts and ends with ```)
    if block.startswith("```") and block.endswith("```"):
        return "code"

    # Check for quote block (each line starts with >)
    if all(re.match(r"^> ", line) for line in block.split("\n")):
        return "quote"

    # Check for unordered list (each line starts with * or - followed by a space)
    if all(re.match(r"^(\*|-) ", line) for line in block.split("\n")):
        return "unordered_list"

    # Check for ordered list (each line starts with a number followed by ". ")
    lines = block.split("\n")
    if all(re.match(rf"^{i+1}\. ", lines[i]) for i in range(len(lines))):
        return "ordered_list"

    # If none of the conditions match, it's a normal paragraph
    return "paragraph"