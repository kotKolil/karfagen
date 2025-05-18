from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from src.etc.Book import *

class TextLabel(QTextBrowser):
    def __init__(self, app):
        self.app = app

        super().__init__()
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.DragEnter:
            if event.mimeData().hasUrls():
                event.acceptProposedAction()
                return True
        elif event.type() == QEvent.Drop:
            if len(event.mimeData().urls()) == 1:
                print(event.mimeData().urls()[0].toString().split("///")[1])
                self.app.Book = Book(filename = event.mimeData().urls()[0].toString().split("///")[1],  encoding = "UTF-8" ,app = self.app)
                self.app.Book.parses()
                self.app.content.setWindowTitle("Karfagen Book Viewer")
                self.app.pages = self.app.Book.parseBookData()
                self.app.Book.parses()
                self.app.numOfPages = len(self.app.pages)
                self.app.render_page(0)
                self.app.navigationBottomPanel.navigationSlider.setMaximum(self.app.numOfPages)
            return True
        return super().eventFilter(obj, event)