from textnode import TextNode, TextType

def main():
    node = TextNode('this is a text node', TextType.NORMAL, 'http://www.url.com')
    print(node)

if __name__ == '__main__':
    main()
