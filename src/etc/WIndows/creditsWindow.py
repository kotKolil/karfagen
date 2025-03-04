from PyQt5.Qt import *

class creditsWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("credits")

        windowLayout = QHBoxLayout()
        self.text = QLabel()
        self.text.setText("2025 by Treska")

        windowLayout.addWidget(self.text)

        self.setLayout(windowLayout)


