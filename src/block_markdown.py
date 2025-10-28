from  enum import Enum


def markdown_to_blocks(markdown):
    block_split = markdown.split('\n\n')
    markdown_list = []
    for part in block_split:
        part = part.strip()
        if part:
            markdown_list.append(part)
    return markdown_list
    

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'


def block_to_block_type(block):  
    i = 0
    while i < len(block) and block[i] == '#':
        i += 1
    if 1 <= i <= 6 and i < len(block) and block[i] == ' ':
            return BlockType.HEADING
        

    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE

    # split the block into individual lines so we can inspect each line separately
    lines = block.splitlines()

    # If every line starts with '>' treat the block as a quote (block-level '>' markdown)
    if lines and all(line.startswith('>') for line in lines):
        return BlockType.QUOTE
     
    # If every line starts with '- ' treat the block as an unordered list (dash list items)
    if lines and all(line.startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST

    # counts ordered lines
    if lines:
        n = 1
        ok = True
        for line in lines:
            if not line.startswith(f"{n}. "):
                ok = False
                break
            n += 1
        if ok:
            return BlockType.ORDERED_LIST

    # Default: paragraph
    return BlockType.PARAGRAPH