import unittest

from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode("this is **bold** text", TextType.NORMAL)
        split_nodes = split_nodes_delimiter([node], "**")
        self.assertEqual(split_nodes[0], TextNode("this is ", TextType.NORMAL))
        self.assertEqual(split_nodes[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(split_nodes[2], TextNode(" text", TextType.NORMAL))

    def test_split_italic(self):
        node = TextNode("this is *italic* text", TextType.NORMAL)
        split_nodes = split_nodes_delimiter([node], "*")
        self.assertEqual(split_nodes[0], TextNode("this is ", TextType.NORMAL))
        self.assertEqual(split_nodes[1], TextNode("italic", TextType.ITALIC))
        self.assertEqual(split_nodes[2], TextNode(" text", TextType.NORMAL))

    def test_split_code(self):
        node = TextNode("this is `code` text", TextType.NORMAL)
        split_nodes = split_nodes_delimiter([node], "`")
        self.assertEqual(split_nodes[0], TextNode("this is ", TextType.NORMAL))
        self.assertEqual(split_nodes[1], TextNode("code", TextType.CODE))
        self.assertEqual(split_nodes[2], TextNode(" text", TextType.NORMAL))

    def test_split_multiple_nodes(self):
        node = TextNode("this is **bold** text", TextType.NORMAL)
        node2 = TextNode("this is normal text", TextType.NORMAL)
        node3 = TextNode("this is more **bold** text again", TextType.NORMAL)
        split_nodes = split_nodes_delimiter([node, node2, node3], "**")
        self.assertEqual(split_nodes[0], TextNode("this is ", TextType.NORMAL))
        self.assertEqual(split_nodes[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(split_nodes[2], TextNode(" text", TextType.NORMAL))
        self.assertEqual(
            split_nodes[3], TextNode("this is normal text", TextType.NORMAL)
        )
        self.assertEqual(split_nodes[4], TextNode("this is more ", TextType.NORMAL))
        self.assertEqual(split_nodes[5], TextNode("bold", TextType.BOLD))
        self.assertEqual(split_nodes[6], TextNode(" text again", TextType.NORMAL))
