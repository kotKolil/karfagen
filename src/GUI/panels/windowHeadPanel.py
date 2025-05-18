from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QMimeData


class windowHead(QToolBar):
    def __init__(self, app):
        super().__init__()
        self.app = app

        # Включаем прием Drag and Drop
        self.setAcceptDrops(True)  # <-- Важно!

        container = QWidget()
        self.layout = QHBoxLayout(container)

        self.layout.setContentsMargins(5, 2, 5, 2)
        self.layout.setSpacing(10)

        self.title_label = QLabel(self.app.langPackage.lang.winTitle)
        self.closeWindowAction = QPushButton("X")
        self.closeWindowAction.clicked.connect(self.close_window)

        self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.closeWindowAction.setFixedSize(20, 20)

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.closeWindowAction)

        self.addWidget(container)

        self.setMovable(False)
        self.setFloatable(False)
        self.setFixedHeight(30)
        self.setMovable(True)


    def close_window(self):
        self.app.content.close()