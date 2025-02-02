import os
from markdown_to_html_node import *
from markdown_extractors import extract_markdown_images, extract_markdown_links
from markdown_blocks import markdown_to_blocks, block_to_block_type


def extract_title(markdown):
    """
    Extracts the first H1 title from markdown.

    Args:
        markdown (str): The markdown content as a string.

    Returns:
        str: The extracted title (without #).

    Raises:
        ValueError: If no H1 header is found.
    """
    for line in markdown.split("\n"):
        if line.startswith("# "):  # Ensure it's an H1
            return line[2:].strip()  # Remove "# " and strip spaces

    raise ValueError("No H1 header found in the markdown file.")

def generate_page(from_path, template_path, dest_path):
    """
    Generates an HTML page from a markdown file using a template.

    Args:
        from_path (str): Path to the markdown file.
        template_path (str): Path to the HTML template.
        dest_path (str): Destination path for the generated HTML.
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown file
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # Read HTML template
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Convert markdown to HTML
    html_body = markdown_to_html_node(markdown_content).to_html()

    # Extract the title
    title = extract_title(markdown_content)

    # Replace placeholders
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_body)

    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the final HTML file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"Page generated successfully: {dest_path}")