from htmlnode import *
from block_markdown import *
from textnode import *
from text_node_to_html_node import text_node_to_html_node
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE:
            code = code_tags(block)
            children.append(code)
        elif block_type == BlockType.HEADING:
            heading = heading_to_html(block)
            children.append(heading)
        elif block_type == BlockType.QUOTE:
            quote = quote_to_html(block)
            children.append(quote)
        elif block_type == BlockType.UNORDERED_LIST:
            unordered = unordered_to_html(block)
            children.append(unordered)
        elif block_type == BlockType.ORDERED_LIST:
            ordered = ordered_to_html(block)
            children.append(ordered)
        elif block_type == BlockType.PARAGRAPH:
            paragraph = paragraph_to_html(block)
            children.append(paragraph)
        else:
            raise Exception("Incorrect block formatting")
    parent = ParentNode('div', children=children)
    return parent    

def code_tags(block):
    raw = block[3:-3]
    if raw.startswith("\n"):
        raw = raw[1:]
    
    lines = raw.split("\n")
    non_empty = [ln for ln in lines if ln.strip() != ""]
    if non_empty:
        def leading_spaces(s):
            i = 0
            while i < len(s) and s[i] == " ":
                i += 1
            return i
        common = min(leading_spaces(ln) for ln in non_empty)
        lines = [ln[common:] if len(ln) >= common else ln for ln in lines]
    raw = "\n".join(lines)
    # ensure trailing newline
    if not raw.endswith("\n"):
        raw += "\n"

    code_leaf = text_node_to_html_node(TextNode(raw, TextType.CODE))
    return ParentNode("pre", children=[code_leaf])

    # block_type = block_to_block_type(block)      
    # if block_type == BlockType.CODE:
    #    raw = block[3:-3]
    #     text_node = TextNode(raw, TextType.CODE)
    #     code_node = text_node_to_html_node(text_node)
    # else:
    #     raise Exception("Not a BlockType.CODE")
    
    
    # parent_code_node = ParentNode("pre", children=[code_node])
    # return parent_code_node

def text_to_children(text):
    list_of_text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in list_of_text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

def heading_to_html(block):
    i = 0
    while i < len(block) and block[i] == '#':
        i += 1
    if i == 0 or i > 6:
        raise Exception("invalid heading block")
    
    #after_hashes = block[i+1:]
    text = block[i:].lstrip()
    children = text_to_children(text)
    html_tag = f"h{i}"
    node = ParentNode(html_tag, children=children)
    return node

def quote_to_html(block):
    lines = block.split("\n")
    cleaned = []
    for line in lines:
        line = line.lstrip()
        if line.startswith("> "):
            cleaned.append(line[2:])
        elif line.startswith(">"):
            cleaned.append(line[1:])
        else:
            cleaned.append(line)
        
    text = " ".join(s.strip() for s in cleaned if s.strip())
    children = text_to_children(text)
    node = ParentNode("blockquote", children=children)
    return node

def unordered_to_html(block):
    lines = block.split('\n')
    nodes_list = []
    for line in lines:
        text = line.lstrip("- ")
        children = text_to_children(text)
        node = ParentNode("li", children=children)
        nodes_list.append(node)
    html_node = ParentNode("ul", children=nodes_list)
    return html_node

def ordered_to_html(block):
    lines = block.split('\n')
    nodes_list = []
    for line in lines:
        split_list = line.split('.', maxsplit=1)
        text = split_list[1].strip()
        children = text_to_children(text)
        node = ParentNode("li", children=children)
        nodes_list.append(node)
    html_node = ParentNode("ol", children=nodes_list)
    return html_node

def paragraph_to_html(block):
    lines = [l.strip() for l in block.split("\n")]
    text = " ".join([l for l in lines if l])
    children = text_to_children(text)
    node = ParentNode("p", children=children)
    return node