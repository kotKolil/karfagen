from PyQt5.Qt import *

class ReadmeWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.resize(0,0)
        self.setFixedHeight(500)
        self.setFixedWidth(500)

        with open("readme.md") as file:
            self.licenseText = file.read()

        self.setWindowTitle("readme")

        windowLayout = QHBoxLayout()
        self.text = QTextBrowser()
        self.text.setText(self.licenseText)

        windowLayout.addWidget(self.text)

        self.setLayout(windowLayout)


