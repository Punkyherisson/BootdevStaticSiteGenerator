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
if __name__ == "__main__":
    unittest.main()