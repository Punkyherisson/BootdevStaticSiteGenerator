from markdown_to_html_node import markdown_to_html_node


def test_markdown_to_html_node():
    markdown = "# Heading\nParagraph with **bold** text."
    html_node = markdown_to_html_node(markdown)
    
    assert html_node.tag == "div"
    assert len(html_node.children) == 2
    assert html_node.children[0].tag == "h1"
    assert html_node.children[1].tag == "p"
    
    print("All tests passed!")

test_markdown_to_html_node()