import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        actual = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(actual, expected)

    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError) as e:
            node = ParentNode(
                None,
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
            node.to_html()
        self.assertEqual(str(e.exception), "tag is required for ParentNode")

    def test_to_html_no_children(self):
        with self.assertRaises(ValueError) as e:
            node = ParentNode(
                "p",
                [],
            )
            node.to_html()
        self.assertEqual(str(e.exception), "children required for ParentNode")
