import re


def extract_markdown_images(text):
    # example: ![rick roll](https://i.imgur.com/aKaOqIh.gif)
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    # example: [to boot dev](https://www.boot.dev)
    # (?<!...) is negative lookbehidn assertion
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)
