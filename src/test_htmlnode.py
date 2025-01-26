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
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    # Existing HTMLNode tests...

    # Test rendering of a LeafNode with tag and value
    def test_leafnode_with_tag_and_value(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    # Test rendering of a LeafNode with tag, value, and props
    def test_leafnode_with_tag_value_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    # Test rendering of a LeafNode with no tag (raw text)
    def test_leafnode_without_tag(self):
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    # Test LeafNode with missing value (should raise ValueError)
    def test_leafnode_no_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

if __name__ == "__main__":
    unittest.main()