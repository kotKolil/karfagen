import sys
from xml.dom.minidom import parse
from PyQt5.Qt import *
import base64

class Book(object):

    def __init__(self, filename, encoding, app):

        self.app = app

        self.parsedTextData = None
        self.filename = filename
        self.encoding = encoding

        self.text_data = None
        self.document = None

        self.genre = None
        self.author = None
        self.title = None
        self.lang = None

    def parse(self):
        global text_nodes
        document = parse(self.filename)

        self.document = document
        self.genre = self.loadTagValueFromXML("genre")
        self.lang = self.loadTagValueFromXML("lang")
        self.author = self.loadTagValueFromXML("last-name") + self.loadTagValueFromXML("first-name")
        self.title = self.loadTagValueFromXML("book-title")

        paragraphs = document.getElementsByTagName("section")
        text_nodes = []
        for paragraph in paragraphs:
            # text_nodes = [
            #     node.childNodes[0].nodeValue for node in paragraph.childNodes
            #     if node.nodeName == 'p' and node.childNodes[0].nodeValue
            # ]
            for node in paragraph.childNodes:
                if node.nodeName == "p" and node.childNodes[0].nodeValue:
                    text_nodes.append(node.childNodes[0].nodeValue)
                else:
                    for ii in node.childNodes:
                        if ii.nodeName == "image":
                            ImageObject = QPixmap.fromImage(self.getImageFromXMLById(ii.getAttribute("l:href")[1:]))
                            text_nodes.append(ImageObject)

        self.text_data = text_nodes
        self.parsedTextData = []

    def getImageFromXMLById(self, imgId):
        for tag in self.document.getElementsByTagName("binary"):
            if tag.getAttribute("id") == imgId:
                img = QImage()
                binStr = tag.childNodes[0].nodeValue.encode("utf-8")
                img.loadFromData(binStr)
                return img
    def loadTagValueFromXML(self, tag_name):
        try:
            tag = self.document.getElementsByTagName(tag_name)[0].childNodes[0].nodeValue
            return tag
        except IndexError:
            return ""



    def parseBookData(self):
        """
        Parses raw book data into pages, handling paragraph wrapping and page breaks.

        Returns:
            A list of pages, where each page is a list of strings (paragraphs/lines).
        """

        pages= []
        page = []
        current_text_height = 0
        font_metrics = QFontMetrics(self.app.appFont)

        for paragraph in self.text_data:
            # Split paragraph into lines that fit

            paragraph = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + paragraph + "<br>"

            lines = self.split_paragraph_into_lines(paragraph, font_metrics, self.app.textLabel.width())
            for line in lines:
                line_height = font_metrics.height()  # Use actual line height

                if current_text_height + line_height <= self.app.textLabel.height() - 30:
                    page.append(line)
                    current_text_height += line_height
                else:
                    pages.append(page)
                    page = [line]
                    current_text_height = line_height  # Reset height to the current line's height

        # Add the last page if it's not empty
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
    widget = QWidget()
    b = Book("C:\\Users\\Treska\\Documents\\projects\\karfagen\\samples\\sampleWithImage.fb2", "UTF-8", app)
    b.parse()
    img = QPixmap.fromImage(b.loadTagValueFromXML("img_0"))
    label = QLabel()
    label.setPixmap(img.scaledToWidth(500, Qt.SmoothTransformation))
    layout = QHBoxLayout()
    layout.addWidget(label)
    widget.setLayout(layout)
    widget.show()
    app.exec_()