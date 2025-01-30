class TextType:
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"

class TextNode:
    def __init__(self, text, text_type):
        self.text = text
        self.text_type = text_type

    def __repr__(self):
        return f'TextNode("{self.text}", {self.text_type})'

    def __eq__(self, other):
        return (
            isinstance(other, TextNode) and
            self.text == other.text and
            self.text_type == other.text_type
        )

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Non-text nodes are added directly
            new_nodes.append(node)
            continue
        if not node.text:
            # If the text is empty, simply append the original node
            new_nodes.append(node)
            continue
            
        # Split the text by the delimiter
        parts = node.text.split(delimiter)
        
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")
        
        for i, part in enumerate(parts):
            if i % 2 == 0:
                # Regular text (outside delimiters)
                if part:
                    new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Text inside delimiters
                new_nodes.append(TextNode(part, text_type))
    
    return new_nodes