from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextType

def text_node_to_html_node(text_node):
    TAG_MAP = {
    TextType.TEXT: None,
    TextType.BOLD: "b",
    TextType.ITALIC: "i",
    TextType.CODE: "code",
    }

    if text_node.text_type in TAG_MAP: 
        return LeafNode(tag=TAG_MAP[text_node.text_type], value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href":text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src":text_node.url, "alt":text_node.text})
    else:
        raise ValueError(f"Unknown TextType: {text_node.text_type}")