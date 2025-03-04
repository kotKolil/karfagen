from src.etc.WIndows.licenseWindows import *
from src.etc.WIndows.readme import *
from src.etc.WIndows.creditsWindow import *

class openInfoMenu(QMenu):
    def __init__(self, app):
        super().__init__()

        self.app = app

        infoBtn = QAction("&about", self)
        self.licenceWindows = licenceWindow()
        infoBtn.triggered.connect(self.licenceWindows.show)
        self.addAction(infoBtn)

        readmeBtn = QAction("&readme", self)
        self.readmeWindows = readmeWindow()
        readmeBtn.triggered.connect(self.readmeWindows.show)
        self.addAction(readmeBtn)


        creditBtn = QAction("&credits", self)
        creditBtn.triggered.connect(self.creditsMessageBox)
        self.addAction(creditBtn)

    def creditsMessageBox(self):

        msg = QMessageBox()
        msg.setWindowTitle("credits")
        msg.setText("2025 by Treska")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()