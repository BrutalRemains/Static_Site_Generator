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
        

    if block.startswith('```') and block.endwith('```'):
        return BlockType.CODE

    if block.startswith('>'):
        return BlockType.QUOTE
    
    if block.startswith('- '):
        return BlockType.UNORDERED_LIST

    if block.startswith('. '):
        return BlockType.ORDERED_LIST

    # Default: paragraph
    return BlockType.PARAGRAPH