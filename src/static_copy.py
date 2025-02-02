import os
import shutil

def copy_directory(src, dest):
    """
    Recursively copies the contents of the src directory to the dest directory.
    
    It first deletes any existing contents in the dest directory, then copies
    all files and subdirectories from src to dest. It logs the path of each file copied.
    
    Args:
        src (str): The source directory (e.g., "static").
        dest (str): The destination directory (e.g., "public").
    """
    # Check if the destination directory exists; if so, delete it.
    if os.path.exists(dest):
        print(f"Deleting existing directory: {dest}")
        shutil.rmtree(dest)
    
    # Create a fresh destination directory.
    os.makedirs(dest, exist_ok=True)
    print(f"Created directory: {dest}")
    
    # Recursively copy each item in the src directory.
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        # Ignore files like ':Zone.Identifier'
        if item.endswith(":Zone.Identifier"):
            continue
        
        if os.path.isdir(src_path):
            print(f"Entering directory: {src_path}")
            copy_directory(src_path, dest_path)  # Recursively copy subdirectories.
        else:
            print(f"Copying file: {src_path} -> {dest_path}")
            shutil.copy(src_path, dest_path)

def main():
    """
    Main function to copy all static content to the public directory.
    """
    src_dir = "static"     # Source directory with static assets.
    dest_dir = "public"    # Destination directory where generated site lives.
    copy_directory(src_dir, dest_dir)
    print("Static content copied successfully!")

if __name__ == "__main__":
    main()