from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    self_closing_tags = {"img", "br"}

    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        self.require_closing_tag = tag not in LeafNode.self_closing_tags

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf nodes must have a value")

        if self.tag is None:
            return self.value

        result = f"<{self.tag}{self.props_to_html()}>{self.value}"
        if self.require_closing_tag:
            result += f"</{self.tag}>"
        return result
