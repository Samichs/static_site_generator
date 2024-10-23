import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    # LeafNode(tag, value, props)
    def test_leafnode_no_props_no_tag(self):
        node = LeafNode(None, "test_node_1", None)
        self.assertEqual(node.to_html(), "test_node_1")

    def test_leafnode_no_props(self):
        node = LeafNode("p", "test_node_1", None)
        self.assertEqual(node.to_html(), "<p>test_node_1</p>")

    def test_leafnode_props_tag(self):
        node = LeafNode("a", "test_node_1", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">test_node_1</a>'
        )
