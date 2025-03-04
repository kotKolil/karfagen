from PyQt5.Qt import *

from src.etc.

class aiReadingMenu(QMenu):

    def __init__(self):
        super().__init__()

        self.startReading = QAction("start")
        self.addAction(self.startReading)
