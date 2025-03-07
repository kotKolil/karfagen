from src.GUI.menus.recentFilesMenu import *
from src.etc.recentFilesParser import *

class openFileMenu(QMenu):
    def __init__(self, app):

        super().__init__()

        self.app = app
        self.recentFilesParser = recentFilesParser()

        openFile = QAction("&open file", self.app)
        openFile.triggered.connect(self.openFileFunc)

        recentFilesClass = recentFilesMenu(self.app)
        recentFiles = QAction("&recent files", self.app)
        recentFiles.setMenu(recentFilesClass)

        self.addAction(openFile)
        self.addAction(recentFiles)

    def openFileFunc(self):
        options = QFileDialog.Options()

        # Get the file names from the dialog
        files, _ = QFileDialog.getOpenFileNames(self.app.content,
                                                "Select Fiction Book Files",
                                                "",
                                                "Fiction Book 2 (*.fb2);;All Files (*)",
                                                options=options)
        if files:
            self.app.Book = Book(filename = files[0], encoding = "UTF-8" ,app = self.app)
            self.app.Book.parse()
            self.app.content.setWindowTitle(self.app.Book.title + " " + self.app.Book.author + " " +
                                            "Karfagen Book Viewer")
            self.app.pages = self.app.Book.parseBookData()
            self.app.Book.parse()
            self.app.numOfPages = len(self.app.pages)
            self.app.render_page(0)
            self.app.navigationBottomPanel.navigationSlider.setMaximum(self.app.numOfPages)
            self.recentFilesParser.addFile(files[0])