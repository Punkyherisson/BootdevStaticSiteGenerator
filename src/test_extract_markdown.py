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

# Run tests
test_extract_markdown_images()
test_extract_markdown_links()
print("All tests passed!")