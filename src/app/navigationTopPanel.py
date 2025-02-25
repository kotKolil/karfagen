from src.Book import *
from PyQt5.Qt import *

from .settingsWindow import *


class navigationTopPanel:

    def __init__(self, app):
        self.app = app

        self.navigationTopPanel = QWidget()
        self.navigationTopPanelLayout = QHBoxLayout()
        self.navigationTopPanel.setLayout(self.navigationTopPanelLayout)

        self.openFile = QPushButton(text="open file")
        self.openFile.clicked.connect(self.openFileFunc)
        self.openFile.setFixedWidth(70)
        self.navigationTopPanelLayout.addWidget(self.openFile)

        self.settingsButton = QPushButton(text="settings")
        self.settingsButton.clicked.connect(settingsWindow().start)
        self.navigationTopPanelLayout.addWidget(self.settingsButton)

        self.navigationTopPanelLayout.setAlignment(Qt.AlignLeft)

    def openFileFunc(self):
        options = QFileDialog.Options()

        # Get the file names from the dialog
        files, _ = QFileDialog.getOpenFileNames(self.app.content,
                                                "Select Fiction Book Files",
                                                "",
                                                "Fiction Book 2 (*.fb2);;All Files (*)",
                                                options=options)
        if files:
            self.app.Book = Book(files[0])
            self.app.Book.parse()

            self.app.content.setWindowTitle(self.app.Book.title + " " + self.app.Book.author + " " + "Karfagen Book Viewer")
            self.app.pages = self.app.Book.parseBookData()
            self.app.numOfPages = len(self.app.pages)
            self.app.render_page(self.app.pageNumber)
            self.app.navigationSlider.setMaximum(self.app.numOfPages)