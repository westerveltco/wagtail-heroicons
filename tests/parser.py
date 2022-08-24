from __future__ import annotations

from html.parser import HTMLParser


class SVGParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found_id = False
        self.id = None

    def handle_starttag(self, tag, attrs):
        if tag == "svg":
            for attr in attrs:
                if "id" in attr:
                    self.found_id = True
                    self.id = attr[1]
