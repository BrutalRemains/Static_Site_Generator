import unittest
from text_to_textnodes import *


class TestTextToTextNode(unittest.TestCase):
    def test_text_bold_with_link(self):
        text = "This is **link** to [Boot.dev](https://boot.dev), okay?"
        nodes = text_to_textnodes(text)
        expected = [
    TextNode("This is ", TextType.TEXT),
    TextNode("link", TextType.BOLD),
    TextNode(" to ", TextType.TEXT),
    TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
    TextNode(", okay?", TextType.TEXT),
]
        self.assertEqual(nodes,expected)

    def test_text_italic_with_link(self):
        text = "This is _link_ to [Boot.dev](https://boot.dev), okay?"
        nodes = text_to_textnodes(text)
        expected = [
    TextNode("This is ", TextType.TEXT),
    TextNode("link", TextType.ITALIC),
    TextNode(" to ", TextType.TEXT),
    TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
    TextNode(", okay?", TextType.TEXT),
]
        self.assertEqual(nodes,expected)
   
    def test_text_italic_with_image(self):
        text = "This is _link_ to ![Boot.dev](https://boot.dev), okay?"
        nodes = text_to_textnodes(text)
        expected = [
    TextNode("This is ", TextType.TEXT),
    TextNode("link", TextType.ITALIC),
    TextNode(" to ", TextType.TEXT),
    TextNode("Boot.dev", TextType.IMAGE, "https://boot.dev"),
    TextNode(", okay?", TextType.TEXT),
]
        self.assertEqual(nodes,expected)

    def test_text_italic_with_bold(self):
        text = "This is _link_ to **Boot.dev**, okay?"
        nodes = text_to_textnodes(text)
        expected = [
    TextNode("This is ", TextType.TEXT),
    TextNode("link", TextType.ITALIC),
    TextNode(" to ", TextType.TEXT),
    TextNode("Boot.dev", TextType.BOLD),
    TextNode(", okay?", TextType.TEXT),
]
        self.assertEqual(nodes,expected)