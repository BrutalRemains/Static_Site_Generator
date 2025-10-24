import unittest
from extract_markdown import *

class TestImageSearch(unittest.TestCase):
    def test_img_empty(self):
        text = "Hello, my name is Krob"
        srch = extract_markdown_images(text)
        self.assertEqual(srch, [])
    def test_multiple_img(self):
        text = "Hello ![hi](https://google.com) and goodbye ![bye](https://bing.com)"
        srch = extract_markdown_images(text)
        self.assertEqual(srch, [('hi', 'https://google.com'), ('bye', 'https://bing.com')])
    def test_no_alt(self):
        text = "Hello ![](https://google.com)"
        srch = extract_markdown_images(text)
        self.assertEqual(srch, [('', 'https://google.com')])
    def test_no_url(self):
        text = "Hello ![hi]()"
        srch = extract_markdown_images(text)
        self.assertEqual(srch, [('hi', '')])

class TestLinkSearch(unittest.TestCase):
    def test_link(self):
        text = "The best website ever is [boot.dev](https://www.boot.dev)"
        srch = extract_markdown_links(text)
        self.assertEqual(srch, [('boot.dev', 'https://www.boot.dev')])
    def test_multiple_links(self):
        text = "The best website ever to learn [python](https://python.org) is [boot.dev](https://www.boot.dev)"
        srch = extract_markdown_links(text)
        self.assertEqual(srch, [('python', 'https://python.org'), ('boot.dev', 'https://www.boot.dev')])
    def test_empty_alt(self):
        text = "The best website ever is [](https://www.boot.dev)"
        srch = extract_markdown_links(text)
        self.assertEqual(srch, [('', 'https://www.boot.dev')])
    def test_no_url(self):               
        text = "The best website ever is [boot.dev]()"
        srch = extract_markdown_links(text)
        self.assertEqual(srch, [('boot.dev', '')])