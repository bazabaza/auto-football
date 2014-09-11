import os

__author__ = 'baza'

from lxml import etree

from autofootball.langtools import cached_property


class FootballImage():
    @cached_property
    def field_tree(self):
        path = os.path.join(os.path.dirname(__file__), 'field.svg')
        with open(path, 'r', encoding='utf-8') as f:
            return etree.parse(f)

    @cached_property
    def svg_elem(self):
        return self.field_tree.getroot()

    def __init__(self):
        self.last_x, self.last_y = 300, 200

    def add_line(self, x, y):
        line_elem = etree.Element(
            'line', {
                'x1': str(self.last_x),
                'y1': str(self.last_y),
                'x2': str(x),
                'y2': str(y),
                'stroke': 'black',
                'stroke-width': '2'
            }
        )
        self.svg_elem.append(line_elem)

        self.last_x, self.last_y = x, y

        return self

    def generate(self, image_format='svg'):
        return etree.tostring(self.field_tree, xml_declaration=True, encoding='utf-8', pretty_print=True)


img = FootballImage()
img.add_line(100, 100).add_line(100, 200).add_line(44, 217)

svg = img.generate()

print(svg)
with open('temp.svg', 'wb') as f:
    f.write(svg)
