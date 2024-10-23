import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        node = HTMLNode("p", "test_node_1", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_2(self):
        node = HTMLNode(
            "a",
            "test_node_2",
            None,
            {"test_tag": "test_value", "test_tag2": "test_value2"},
        )
        self.assertEqual(
            node.props_to_html(), ' test_tag="test_value" test_tag2="test_value2"'
        )

    def test_props_to_html_3(self):
        node3 = HTMLNode("a", "test_url_node", None, {"href": "http://www.url.com"})
        node2 = HTMLNode("p", "test_paragraph_node", [node3], None)
        node = HTMLNode("h1", "test_header_node", [node2], None)
        self.assertEqual(node3.props_to_html(), ' href="http://www.url.com"')
