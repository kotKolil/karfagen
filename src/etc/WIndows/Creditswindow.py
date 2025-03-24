from PyQt5.Qt import *

class CreditWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("credits")

        window_layout = QHBoxLayout()
        self.text = QLabel()
        self.text.setText("2025 by Treska")

        window_layout.addWidget(self.text)

        self.setLayout(window_layout)


