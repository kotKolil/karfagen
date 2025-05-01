from src.etc.WIndows.licenseWindows import *
from src.etc.WIndows.readme import *
from src.etc.WIndows.Creditswindow import *


def creditsMessageBox():

    msg = QMessageBox()
    msg.setWindowTitle("credits")
    msg.setText("2025 by Treska")
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


class openInfoMenu(QMenu):
    def __init__(self, app):
        super().__init__()

        self.app = app

        infoBtn = QAction("&" + self.app.langPackage.lang.about, self)
        self.licenceWindows = LicenceWindow()
        infoBtn.triggered.connect(self.licenceWindows.show)
        self.addAction(infoBtn)

        readmeBtn = QAction("&" + self.app.langPackage.lang.readme, self)
        self.readmeWindows = ReadmeWindow()
        readmeBtn.triggered.connect(self.readmeWindows.show)
        self.addAction(readmeBtn)


        creditBtn = QAction("&" + self.app.langPackage.lang.credits, self)
        creditBtn.triggered.connect(creditsMessageBox)
        self.addAction(creditBtn)

