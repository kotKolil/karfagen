import json
import os

from src.etc.Book import *
from src.etc.recentFilesParser import *


class recentFilesMenu(QMenu):

    def __init__(self, app):

        super().__init__()

        self.app = app

        data = recentFilesParser()
        print(data.data)
        if len(data.data["recentFiles"]) == 0:
            entries = os.listdir("./samples/")
            for filenames in [os.path.join("./samples/", entry) for entry in entries if
                              os.path.isfile(os.path.join("./samples/", entry))]:
                ii = QAction(os.path.basename(filenames), self)
                ii.triggered.connect(lambda filename=filenames: self.openFile(filenames))
                self.addAction(ii)
        else:
            for filenames in data.data["recentFiles"]:
                ii = QAction(os.path.basename(filenames), self)
                ii.triggered.connect(lambda filename=filenames: self.openFile(filenames))
                self.addAction(ii)

    def openFile(self, filename):
        print("хуй")
        print(filename)
        self.app.Book = Book(filename=filename, encoding="UTF-8", app=self.app)
        print("хуй")
        self.app.Book.parse()
        print("хуй")
        self.app.content.setWindowTitle(self.app.Book.title + " " + self.app.Book.author + " " +
                                        "Karfagen Book Viewer")
        self.app.pages = self.app.Book.parseBookData()
        self.app.Book.parse()
        self.app.numOfPages = len(self.app.pages)
        self.app.render_page(0)
        self.app.navigationBottomPanel.navigationSlider.setMaximum(self.app.numOfPages)