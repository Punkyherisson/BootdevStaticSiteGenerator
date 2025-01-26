import unittest
from htmlnode import *

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

class TestParentNode(unittest.TestCase):
    # Test rendering of a ParentNode with multiple LeafNode children
    def test_parentnode_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        )

    # Test rendering of a ParentNode with nested ParentNode
    def test_parentnode_with_nested_children(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ]
                ),
                LeafNode("i", "Italic text"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><p><b>Bold text</b>Normal text</p><i>Italic text</i></div>"
        )

    # Test ParentNode without a tag (should raise ValueError)
    def test_parentnode_without_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [])

    # Test ParentNode without children (should raise ValueError)
    def test_parentnode_without_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None)

    # Test ParentNode with empty children list (should raise ValueError)
def test_parentnode_with_empty_children(self):
    with self.assertRaises(ValueError) as context:
        ParentNode("div", [])  # Passing an empty list as children
    self.assertEqual(str(context.exception), "ParentNode must have a non-empty list of children.")

if __name__ == "__main__":
    unittest.main()