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