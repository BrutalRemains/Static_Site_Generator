from textnode import TextType, TextNode
from split_nodes_delimiter import *

text = "This is _link_ to **Boot.dev** okay?"
def text_to_textnodes(text):
    new_node = TextNode(text, TextType.TEXT)
    old_nodes = [new_node]
    split_code = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
    split_bold = split_nodes_delimiter(split_code, "**", TextType.BOLD)
    split_italic = split_nodes_delimiter(split_bold, "_", TextType.ITALIC)    
    split_image = split_nodes_image(split_italic)
    split_link = split_nodes_link(split_image)
    return split_link

print(text_to_textnodes(text))