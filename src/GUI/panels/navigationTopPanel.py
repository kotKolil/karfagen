from src.GUI.menus.openFileMenu import *
from src.GUI.menus.infoMenu import *
from src.etc.WIndows.SettingsWindow import *
from src.etc.Recentfilesparser import *

from PyQt5.Qt import *

class navigationTopPanel(QToolBar):

    def __init__(self, app):
        
        super().__init__()
        self.app = app

        self.openFileButton = QAction("&" + self.app.langPackage.lang.openFile, self)
        self.openFileButton.setMenu(openFileMenu(self.app))
        self.addAction(self.openFileButton)

        self.openInfoButton = QAction("&" + self.app.langPackage.lang.info, self)
        self.openInfoButton.setMenu(openInfoMenu(self.app))
        self.addAction(self.openInfoButton)

        self.openSettingsButton = QAction("&" + self.app.langPackage.lang.settings, self)
        self.openSettingsButton.triggered.connect(self.openSettingsWindow)
        self.addAction(self.openSettingsButton)

    def openSettingsWindow(self):
        self.stClass = SettingsWindow(self.app)
        self.stClass.show()