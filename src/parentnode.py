from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag is required for ParentNode")

        if not self.children:
            raise ValueError("children required for ParentNode")

        return f"<{self.tag}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
