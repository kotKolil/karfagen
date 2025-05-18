from src.GUI.menus.recentFilesMenu import *
from src.etc.Recentfilesparser import *

class openFileMenu(QMenu):
    def __init__(self, app):

        super().__init__()

        self.app = app
        self.recentFilesParser = Recentfilesparser()

        openFile = QAction("&" + self.app.langPackage.lang.openFileButton, self.app)
        openFile.triggered.connect(self.openFileFunc)

        recentFilesClass = recentFilesMenu(self.app)
        recentFiles = QAction("&"  + self.app.langPackage.lang.recentFiles, self.app)
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
            print(files[0])
            print(type(files[0]))
            self.app.Book = Book(filename = files[0], encoding = "UTF-8" ,app = self.app)
            self.app.Book.parses()
            self.app.content.setWindowTitle(
                                            "Karfagen Book Viewer")
            self.app.pages = self.app.Book.parseBookData()
            self.app.Book.parses()
            self.app.numOfPages = len(self.app.pages)
            self.app.render_page(0)
            self.app.navigationBottomPanel.navigationSlider.setMaximum(self.app.numOfPages)
            self.recentFilesParser.addFile(files[0])