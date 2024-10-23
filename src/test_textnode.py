import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "not_None_url")
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode(
            "This is a text node", TextType.BOLD, "http://www.thisisaurl.com"
        )
        expected = f"TextNode({node.text}, {node.text_type}, {node.url})"
        self.assertEqual(expected, repr(node))

    def test_text_node_to_html_node_normal(self):
        text_node = TextNode("normal text", TextType.NORMAL)
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node.to_html(), "normal text")

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("bold text", TextType.BOLD)
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node.to_html(), "<b>bold text</b>")

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("italic text", TextType.ITALIC)
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node.to_html(), "<i>italic text</i>")

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("code text", TextType.CODE)
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node.to_html(), "<code>code text</code>")

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("link text", TextType.LINK, "http://www.url.com")
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(
            converted_node.to_html(), '<a href="http://www.url.com">link text</a>'
        )

    def test_text_node_to_html_node_image(self):
        text_node = TextNode(
            "image alt text", TextType.IMAGE, "http://www.image_url.com"
        )
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(
            converted_node.to_html(),
            '<img src="http://www.image_url.com" alt="image alt text">',
        )


if __name__ == "__main__":
    unittest.main()
