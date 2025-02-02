from extract_markdown import *

def test_extract_markdown_images():
    text = "Image 1: ![Alt 1](https://example.com/img1.png), Image 2: ![Alt 2](https://example.com/img2.jpg)"
    assert extract_markdown_images(text) == [
        ("Alt 1", "https://example.com/img1.png"),
        ("Alt 2", "https://example.com/img2.jpg"),
    ]
    
    text = "No images here!"
    assert extract_markdown_images(text) == []

def test_extract_markdown_links():
    text = "Link 1: [Google](https://google.com), Link 2: [GitHub](https://github.com)"
    assert extract_markdown_links(text) == [
        ("Google", "https://google.com"),
        ("GitHub", "https://github.com"),
    ]
    
    text = "Some text with no links."
    assert extract_markdown_links(text) == []
    
    text = "Text with an image link: ![Alt](https://example.com/img.png)"
    assert extract_markdown_links(text) == []

def test_markdown_to_blocks():
    markdown = """# Heading 1

    This is a paragraph with **bold** text.

    * Item 1
    * Item 2
    * Item 3

    """
    result = markdown_to_blocks(markdown)
    print("Actual result:", result)  # Add this line
    assert result == [
        "# Heading 1",
        "This is a paragraph with **bold** text.",
        "* Item 1\n* Item 2\n* Item 3"
    ]

    # Edge case: Multiple empty lines
    markdown = """# Title


    Paragraph with some text.


    * List item 1
    * List item 2


    """
    result = markdown_to_blocks(markdown)
    assert result == [
        "# Title",
        "Paragraph with some text.",
        "* List item 1\n* List item 2"
    ]

    # Edge case: Only empty lines
    markdown = """


    """
    result = markdown_to_blocks(markdown)
    assert result == []

def test_block_to_block_type():
    assert block_to_block_type("### Heading") == "heading"
    assert block_to_block_type("## Subheading") == "heading"
    assert block_to_block_type("```print('Hello World')```") == "code"
    assert block_to_block_type("> Quote line\n> Another quote") == "quote"
    assert block_to_block_type("* Item 1\n* Item 2") == "unordered_list"
    assert block_to_block_type("- Another item\n- More items") == "unordered_list"
    assert block_to_block_type("1. First\n2. Second\n3. Third") == "ordered_list"
    assert block_to_block_type("This is a normal paragraph.") == "paragraph"

    # Edge cases
    assert block_to_block_type("##Not a heading") == "paragraph"  # No space after #
    assert block_to_block_type(">Not a quote") == "paragraph"  # No space after >
    assert block_to_block_type("1.First item\n2.Second item") == "paragraph"  # Missing space after number.
    assert block_to_block_type("```Code start\nCode middle\nCode end```") == "code"  # Multi-line code block

    print("All tests passed!")

def test_extract_title():
    assert extract_title("# Hello") == "Hello"
    assert extract_title("#   Hello World  ") == "Hello World"
    assert extract_title("#Title") == "Title"

    try:
        extract_title("No title here")
    except ValueError as e:
        assert str(e) == "No H1 header found in the markdown file"
# Run the tests

# Run tests
test_extract_markdown_images()
test_extract_markdown_links()
test_markdown_to_blocks()
test_block_to_block_type()
test_extract_title()

print("All tests passed!")