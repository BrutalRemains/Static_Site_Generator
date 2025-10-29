from textnode import TextNode, TextType
from htmlnode import *
from page_generation import *
import sys

def main():
    copy_to_directory('static', 'docs')
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    basepath = basepath.rstrip("/") + "/"
    build_all_content('content', 'template.html', 'docs', basepath)
    

if __name__ == "__main__":
    main()
