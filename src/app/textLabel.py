from PyQt5.Qt import *


class textLabel(object):
    def __init__(self, app):
        self.app = app

        self.textLabel = QLabel()
        self.textLabel.setWordWrap(1)
        self.textLabel.setFixedWidth(400)
        self.textLabel.setFixedHeight(300)
