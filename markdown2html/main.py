

from utils.file import File

class MarkdownElement:
    def to_html(self):
        return ''

class Heading(MarkdownElement):
    def __init__(self, level, text):
        self.level = level
        self.text = text

    def to_html(self):
        return f'<h{self.level}>{self.text}</h{self.level}>'

class Paragraph(MarkdownElement):
    def __init__(self, text):
        self.text = text

    def to_html(self):
        return f'<p>{self.text}</p>'

class Link(MarkdownElement):
    def __init__(self, text, url):
        self.text = text
        self.url = url

    def to_html(self):
        return f'<a href="{self.url}">{self.text}</a>'

def parse_markdown(md_text):
    elements = []
    lines = md_text.strip().split('\n')

    for line in lines:

        if line.startswith('#'):
            level = 0
            while line[level] == '#':
                level += 1
            text = line[level:].strip()
            elements.append(Heading(level, text))

        elif line.startswith('[') and ']' in line and '(' in line:
            start = line.find('[')
            end = line.find(']')
            url_start = line.find('(')
            url_end = line.find(')')
            text = line[start + 1:end]
            url = line[url_start + 1:url_end]
            elements.append(Link(text, url))

        else:
            elements.append(Paragraph(line.strip()))

    return elements


def convert_to_html(elements):
    html_output = ''
    for element in elements:
        html_output += element.to_html() + '\n'
    return html_output


def convert_md_to_html(md_text):
    elements = parse_markdown(md_text)
    html_output = convert_to_html(elements)
    return html_output

def test1():
    input_markdown = File.read_file('./file/test1.md')
    html_result = convert_md_to_html(input_markdown)
    File.write_file('./output/test1.html', html_result)


def test_read_file():
    file = './file/test1.md'
    res = File.read_file(file)
    print(res)

def test_write_file():
    file = './output/test2.html'
    content = '<h1>Hello World</h1>'
    File.write_file(file, content)

def main():
    test1()
    # test_read_file()
    # test_write_file()


if __name__ == '__main__':
    main()
