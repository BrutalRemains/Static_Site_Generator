from textnode import TextType, TextNode
from extract_markdown import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
           new_nodes.append(n)
        else:
            parts = n.text.split(delimiter)
            if len(parts) == 1:
                new_nodes.append(n)
            elif len(parts) % 2 == 0:
                raise Exception("incomplete")
            else:
                for i, part in enumerate(parts):
                    if i % 2 == 0:
                        if part != "":
                            new_nodes.append(TextNode(part, TextType.TEXT))
                    elif part == "":
                        raise Exception("empty inline segment")
                    else:
                        new_nodes.append(TextNode(part, text_type))
        
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            new_nodes.append(n)
            continue 

        
        curr_text = n.text
        
        while True:
            image_srch = extract_markdown_images(curr_text)               
            if not image_srch:
                if curr_text:
                    new_nodes.append(TextNode(curr_text, TextType.TEXT))
                break
        
            alt, url = image_srch[0]
            matched = f'![{alt}]({url})'
            before, after = curr_text.split(matched, 1)
            
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            
            curr_text = after   
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            new_nodes.append(n)
            continue 

        
        curr_text = n.text
            
        while True:
            link_srch = extract_markdown_links(curr_text)               
            if not link_srch:
                if curr_text:
                    new_nodes.append(TextNode(curr_text, TextType.TEXT))
                break
        
            alt, url = link_srch[0]
            matched = f'[{alt}]({url})'
            before, after = curr_text.split(matched, 1)
            
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url))
            
            curr_text = after   
    return new_nodes
