from bs4.element import Comment
from bs4 import BeautifulSoup
import html2text

class BS4_HTMLToTextConverter:
    def __init__(self, html, escaped_tags=['style', 'script', 'head', 'title', 'meta', '[document]']):
        self.html = html
        self.escaped_tags = escaped_tags
        self.text = self._html_to_text(self.html)

    def _tag_visible(self, element):
        if element.parent.name in self.escaped_tags or isinstance(element, Comment):
            return False
        return True

    def _html_to_text(self, body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(self._tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)
    
    def get_text(self):
        return self.text


class html2text_HTMLToTextConverter:
    def __init__(self, html):
        self.html = html
        self.text = self._html_to_text(self.html)

    def _html_to_text(self, page):
        return html2text.html2text(page)
   
    def get_text(self):
        return self.text
