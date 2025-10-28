import unittest
from block_markdown import *
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_code_blocks(self):
        block = "```Hello, World```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    def test_code_blocks_edge(self):
        block = "``Hello, World```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)    
    def test_quote_blocks(self):
        block = "> Hello, World"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    def test_quote_unordered_list(self):
        block = "- Hello, World"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    def test_quote_ordered_list(self):
        block = "1. Hello, World\n2. Again\n3. Signed\4. Kristian"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
    def test_quote_ordered_list_edge(self):
        block = "1.Hello, World\n2. Again\n3. Signed\4. Kristian"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_heading(self):
        block = "###### Hello World"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    def test_heading_edge_no_space(self):
        block = "######Hello World"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_heading_edge_7_hash(self):
        block = "####### Hello World"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
        
    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )