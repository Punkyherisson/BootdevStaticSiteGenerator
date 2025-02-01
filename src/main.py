from text_node import TextNode, TextType

def main():
    # Create a TextNode object with dummy values
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()