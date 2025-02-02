import os
import shutil
from static_copy import copy_directory
from text_node import TextNode, TextType

def main():
    # Dynamically set paths relative to script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(script_dir, "../static")
    public_dir = os.path.join(script_dir, "../public")

    # Clear the public directory by copying static assets
    copy_directory(static_dir, public_dir)

    # Example TextNode usage
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()