import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    # Test for equality when all properties are the same
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    # Test for inequality when text property is different
    def test_neq_text(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    # Test for inequality when text_type property is different
    def test_neq_text_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    # Test for equality when url property is None (default value)
    def test_eq_with_default_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node1, node2)

    # Test for inequality when url property is different
    def test_neq_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://different.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()