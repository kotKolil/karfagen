from PyQt5.Qt import *

class licenceWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.resize(0,0)
        self.setFixedHeight(500)
        self.setFixedWidth(500)

        with open("license.txt") as file:
            self.licenseText = file.read()

        self.setWindowTitle("license")

        windowLayout = QHBoxLayout()
        self.text = QTextBrowser()
        self.text.setText(self.licenseText)

        windowLayout.addWidget(self.text)

        self.setLayout(windowLayout)


