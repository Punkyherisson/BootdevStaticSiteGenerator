from text_to_textnodes import text_to_textnodes
from text_node import TextNode, TextType

def test_text_to_textnodes():
    text = "This is **bold** and *italic* text with `code`."
    nodes = text_to_textnodes(text)
    # Print the nodes to see what we get
    for node in nodes:
        print(node)

def test_text_to_textnodes_with_links_and_images():
    text = "This is a [link](https://boot.dev) and an ![image](https://image.url)"
    nodes = text_to_textnodes(text)
    for node in nodes:
        print(node)

if __name__ == "__main__":
    test_text_to_textnodes()
    test_text_to_textnodes_with_links_and_images()