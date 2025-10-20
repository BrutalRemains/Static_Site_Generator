import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


# class TestHTMLNode(unittest.TestCase):
#     def test_no_props(self):
#         node = HTMLNode("h1", "Hello, World", None, None)
#         self.assertEqual(node.props_to_html(), "")
#     def test_props_formatting(self):
#         node = HTMLNode("a", "Link", None, {"href": "https://x.com", "target": "_blank"})
#         out = node.props_to_html()
#         self.assertIn(' href="https://x.com"', out)
#         self.assertIn(' target="_blank"', out)
#         self.assertTrue(out.startswith(" "))
#     def test_repr(self):
#         parent = HTMLNode("div", None, [HTMLNode("p", "a"), HTMLNode("p", "b")], None)
#         rep = repr(parent)
#         self.assertIn("children=2", rep)
    
# class TestLeafNode(unittest.TestCase):
#     def test_leaf_to_html_p(self):
#         node = LeafNode("p", "Hello, world!")
#         self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
#     def test_leaf_h1(self):
#         node = LeafNode("h1", "Hello, world!")
#         self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")
#     def test_leaf_link(self):
#         node = LeafNode("p", "Google", {"href": "https://www.google.com"})
#         self.assertEqual(node.to_html(), '<p href="https://www.google.com">Google</p>')

# class TestParentNode(unittest.TestCase):
#     def test_to_html_with_children(self):
#         child_node = LeafNode("span", "child")
#         parent_node = ParentNode("div", [child_node])
#         self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")    
#     def test_to_html_with_grandchildren(self):
#         grandchild_node = LeafNode("b", "grandchild")
#         child_node = ParentNode("span", [grandchild_node])
#         parent_node = ParentNode("div", [child_node])
#         self.assertEqual(
#             parent_node.to_html(),
#             "<div><span><b>grandchild</b></span></div>",
#         )
#     def test_to_html_with_great_grandchildren(self):
#         great_grandchild_node = LeafNode("b", "hello world")
#         grandchild_node = ParentNode("h4", [great_grandchild_node])
#         child_node = ParentNode("span", [grandchild_node])
#         parent_node = ParentNode("div", [child_node])
#         self.assertEqual(
#             parent_node.to_html(),
#             "<div><span><h4><b>hello world</b></h4></span></div>",
#         )
#     def test_to_html_with_no_tag(self):
#         child_node = LeafNode("span", "child")
#         parent_node = ParentNode(None, [child_node])
#         with self.assertRaisesRegex(ValueError, "Tag needed!"):
#             parent_node.to_html() 
#     def test_to_html_no_child(self):
#         parent_node = ParentNode("div", None)
#         with self.assertRaisesRegex(ValueError, "Children needed"):
#             parent_node.to_html() 