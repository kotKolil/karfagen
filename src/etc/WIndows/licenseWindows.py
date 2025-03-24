from PyQt5.Qt import *

class LicenceWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.resize(0,0)
        self.setFixedHeight(500)
        self.setFixedWidth(500)

        with open("license.txt") as file:
            self.licenseText = file.read()

        self.setWindowTitle("license")

        window_layout = QHBoxLayout()
        self.text = QTextBrowser()
        self.text.setText(self.licenseText)

        window_layout.addWidget(self.text)

        self.setLayout(window_layout)


