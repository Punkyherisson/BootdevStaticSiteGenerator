import unittest
from split_nodes import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_case(self):
        node = TextNode("Hello `world`!", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.CODE),
            TextNode("!", TextType.TEXT),
        ])

    # Add more tests to cover edge cases!
    def test_no_delimiters(self):
        node = TextNode("No special formatting here.", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])


    def test_unmatched_delimiters_raises(self):
        node = TextNode("Unmatched `delimiter", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)  

    def test_multiple_delimiters(self):
        node = TextNode("Some `code` and more `code`.", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("Some ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and more ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT),
    ])   
    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])


def test_split_nodes_image():
    node = TextNode(
        "Text with an image ![Alt 1](https://example.com/img1.png) and more text.",
        TextType.TEXT,
    )
    result = split_nodes_image([node])
    assert result == [
        TextNode("Text with an image ", TextType.TEXT),
        TextNode("Alt 1", TextType.IMAGE, "https://example.com/img1.png"),
        TextNode(" and more text.", TextType.TEXT),
    ]

    # Test no images
    node = TextNode("No images here!", TextType.TEXT)
    result = split_nodes_image([node])
    assert result == [node]

def test_split_nodes_link():
    node = TextNode(
        "Text with a link [Google](https://google.com) and another [GitHub](https://github.com).",
        TextType.TEXT,
    )
    result = split_nodes_link([node])
    assert result == [
        TextNode("Text with a link ", TextType.TEXT),
        TextNode("Google", TextType.LINK, "https://google.com"),
        TextNode(" and another ", TextType.TEXT),
        TextNode("GitHub", TextType.LINK, "https://github.com"),
        TextNode(".", TextType.TEXT),
    ]

    # Test no links
    node = TextNode("No links here!", TextType.TEXT)
    result = split_nodes_link([node])
    assert result == [node]

# Run tests
'''
test_split_nodes_image()
test_split_nodes_link()
print("All tests passed!")
'''

if __name__ == "__main__":
    unittest.main()