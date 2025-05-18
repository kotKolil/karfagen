import random
import sys
import os
from xml.dom.minidom import parse
from PyQt5.Qt import *
import base64
from PIL import Image
import io

class Book(object):

    def __init__(self, filename, encoding, app):

        self.app = app

        self.parsedTextData = None
        self.filename = filename
        self.encoding = encoding

        try: os.mkdir("images")
        except FileExistsError: pass

        self.text_data = None
        self.document = None

        self.genre = None
        self.author = None
        self.title = None
        self.lang = None

    def parses(self):
        global text_nodes
        document = parse(self.filename)

        self.document = document
        self.genre = self.loadTagValueFromXML("genre")
        self.lang = self.loadTagValueFromXML("lang")
        self.autor = self.loadTagValueFromXML("last-name") + self.loadTagValueFromXML("first-name")
        self.title = self.loadTagValueFromXML("book-title")
        paragraphs = document.getElementsByTagName("section")
        text_nodes = []
        for paragraph in paragraphs:
            for node in paragraph.childNodes:
                if node.nodeName == "p" and node.childNodes[0].nodeValue:
                    text_nodes.append(node.childNodes[0].nodeValue)
                elif node.nodeName == "image":
                    text_nodes.append(self.getImageFromXMLById(node.getAttribute("l:href")[1:]))

        self.text_data = text_nodes
        self.parsedTextData = []

    def getImageFromXMLById(self, imgId):
        for tag in self.document.getElementsByTagName("binary"):
            if tag.getAttribute("id") == imgId:
                binStr = base64.b64decode(tag.childNodes[0].nodeValue)
                imgId = random.randint(10**5+1, 10**6)
                img_path = os.path.join("images", f'{imgId}.jpg')

                # Создаем директорию, если её нет
                os.makedirs("images", exist_ok=True)

                # Сохраняем изображение
                buf = io.BytesIO(binStr)
                image = Image.open(buf)
                new_width = int(self.app.appConfig.WINDOW_WIDTH * 0.7) if image.width >= self.app.appConfig.WINDOW_WIDTH else image.width
                new_height = int(self.app.appConfig.WINDOW_HEIGHT * 0.7) if image.height >= self.app.appConfig.WINDOW_HEIGHT else image.height
                resized_image = image.resize((new_width, new_height))
                resized_image.save(img_path)

                return f"<img src='{img_path}' style='max-width: 100%; max-height: 100%;' />"

    def loadTagValueFromXML(self, tag_name):
        try:
            tag = self.document.getElementsByTagName(tag_name)[0].childNodes[0].nodeValue
            return tag
        except IndexError:
            return ""



    def parseBookData(self):
        pages = []
        page = []
        current_text_height = 0
        font_metrics = QFontMetrics(self.app.appFont)

        for paragraph in self.text_data:
            if isinstance(paragraph, str) and "img" in paragraph:
                # Если текущая страница не пуста, добавляем её в pages
                if page:
                    pages.append(page)
                    page = []
                    current_text_height = 0
                # Добавляем изображение как отдельную страницу
                pages.append([paragraph])
                continue

            # Обработка текстовых параграфов
            paragraph = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + paragraph + "<br>"
            lines = self.split_paragraph_into_lines(paragraph, font_metrics, self.app.textLabel.width())

            for line in lines:
                line_height = font_metrics.height()

                if current_text_height + line_height <= self.app.textLabel.height() - 30:
                    page.append(line)
                    current_text_height += line_height
                else:
                    pages.append(page)
                    page = [line]
                    current_text_height = line_height

        # Добавляем последнюю страницу, если она не пуста
        if page:
            pages.append(page)

        return pages
    def split_paragraph_into_lines(self, paragraph: str, font_metrics: QFontMetrics, max_width: int):
        """
        Splits a paragraph into lines that fit within the maximum width, handling word wrapping.

        Args:
            paragraph: The paragraph to split.
            font_metrics: QFontMetrics object.
            max_width: The maximum width for a line.

        Returns:
            A list of strings, where each string is a line.
        """

        global newString, i
        if font_metrics.horizontalAdvance(paragraph) >= self.app.textLabel.width():

            words = paragraph.split()
            lines = []
            current_line = ""

            for word in words:
                test_line = current_line + word + " "  # Add word and a space to test
                if font_metrics.horizontalAdvance(test_line) <= max_width:
                    current_line = test_line
                else:
                    if current_line:  # Add the current line if it's not empty
                        newString = ""
                        for i in range(len(current_line)):
                            newString += current_line[i]
                            if font_metrics.horizontalAdvance(newString) == max_width:
                                break
                    lines.append(newString)
                    current_line = word + " " + current_line[i:len(current_line)]  # Start a new line with the current word

            if current_line:  # Add the last line
                lines.append(current_line.strip())
            return lines

        else:
            return [paragraph]


if __name__ == "__main__":
    app = QApplication(sys.argv)

    book = Book("C:\\Users\\treska\\Documents\\projects\\karfagen\\samples\\sampleWithImage.fb2", encoding = "UTF-8", app = app)
    book.parses()
    app.render_page(0)

    window = QWidget()
    layout = QHBoxLayout()
    textarea = QTextBrowser()
    layout.addWidget(textarea)
    window.setLayout(layout)
    window.show()
    app.exec_()