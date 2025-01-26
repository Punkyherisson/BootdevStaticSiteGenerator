import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    # Test for props_to_html with multiple attributes
    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com" target="_blank"')

    # Test for props_to_html with no attributes
    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    # Test for props_to_html with a single attribute
    def test_props_to_html_single(self):
        node = HTMLNode(props={"class": "btn-primary"})
        self.assertEqual(node.props_to_html(), ' class="btn-primary"')

    # Test for __repr__ method
    def test_repr(self):
        node = HTMLNode(tag="p", value="This is a paragraph", props={"class": "text"})
        self.assertEqual(
            repr(node), 
            "HTMLNode(tag=p, value=This is a paragraph, children=[], props={'class': 'text'})"
        )

if __name__ == "__main__":
    unittest.main()