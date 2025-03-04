from src.GUI.menus.openFileMenu import *
from src.GUI.menus.infoMenu import *
from src.etc.WIndows.settingsWindow import *

from PyQt5.Qt import *

class navigationTopPanel(QToolBar):

    def __init__(self, app):
        
        super().__init__()
        self.app = app

        self.openFileButton = QAction("&open file", self)
        self.openFileButton.setMenu(openFileMenu(self.app))
        self.addAction(self.openFileButton)

        self.openInfoButton = QAction("info", self)
        self.openInfoButton.setMenu(openInfoMenu(self.app))
        self.addAction(self.openInfoButton)

        self.openSettingsButton = QAction("&settings", self)
        self.openSettingsButton.triggered.connect(self.openSettingsWindow)
        self.addAction(self.openSettingsButton)

    def openSettingsWindow(self):
        self.stClass = settingsWindow(self.app)
        self.stClass.show()