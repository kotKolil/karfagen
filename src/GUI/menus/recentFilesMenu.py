from src.etc.Book import *
from src.etc.Recentfilesparser import *
from functools import partial

class recentFilesMenu(QMenu):

    def __init__(self, app):

        super().__init__()

        self.app = app

        data = Recentfilesparser()
        if len(data.data["recentFiles"]) == 0:
            pass
        else:
            for filename in data.data["recentFiles"]:
                ii = QAction(os.path.basename(filename), self)
                ii.triggered.connect(partial(self.openFile, filename))
                self.addAction(ii)

    def openFile(self, filename):
        print(filename)
        self.app.Book = Book(filename=filename, encoding="UTF-8", app=self.app)
        self.app.Book.parses()
        self.app.content.setWindowTitle("Karfagen Book Viewer")
        self.app.pages = self.app.Book.parseBookData()
        self.app.Book.parses()
        self.app.numOfPages = len(self.app.pages)
        self.app.render_page(0)
        self.app.navigationBottomPanel.navigationSlider.setMaximum(self.app.numOfPages)

    def dropEvent(self, event):
        pass