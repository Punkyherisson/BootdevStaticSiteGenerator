from enum import Enum
from htmlnode import HTMLNode  # Add this line!

# Define the TextType enum
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

# Define the TextNode class
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def to_html_node(self):
        if self.text_type == TextType.TEXT:
            return self.text
        elif self.text_type == TextType.BOLD:
            return HTMLNode(tag="b", children=[self.text])
        elif self.text_type == TextType.ITALIC:
            return HTMLNode(tag="i", children=[self.text])
        elif self.text_type == TextType.CODE:
            return HTMLNode(tag="code", children=[self.text])
        elif self.text_type == TextType.LINK:
            return HTMLNode(tag="a", children=[self.text], props={"href": self.url})
        elif self.text_type == TextType.IMAGE:
            return HTMLNode(tag="img", props={"src": self.url, "alt": self.text})