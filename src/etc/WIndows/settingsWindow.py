from PyQt5.Qt import *
from src.etc.configParser import *

class settingsWindow(QWidget):

    def __init__(self, app):

        self.configClass = configParser()
        self.app = app

        super().__init__()

        self.setStyleSheet(self.configClass.APP_THEME)
        self.setWindowTitle("settings")
        self.setWindowIcon(QIcon("./assets/karfagen.png"))
        self.setFixedSize(400, 400)

        self.settingsWindowBaseLayout = QVBoxLayout()

        self.textSizeField = QLineEdit()
        self.textSizeField.setValidator(QIntValidator())
        self.textSizeField.setText(str(self.configClass.TEXT_SIZE))

        self.windowWidth = QLineEdit()
        self.windowWidth.setValidator(QIntValidator())
        self.windowWidth.setText(str(self.configClass.WINDOW_WIDTH))

        self.windowHeight = QLineEdit()
        self.windowHeight.setValidator(QIntValidator())
        self.windowHeight.setText(str(self.configClass.WINDOW_HEIGHT))

        self.fontType = QComboBox()
        self.fontType.addItems(QFontDatabase().families())
        self.fontType.setCurrentText(str(self.configClass.FONT_NAME))

        self.appStyle = QComboBox()
        self.appStyle.addItems(QStyleFactory.keys())
        self.appStyle.setCurrentText(str(self.configClass.WINDOW_STYLE))

        self.appTheme = QComboBox()
        self.appTheme.addItems(["white", "dark", "console", "sepia"])
        self.appTheme.setCurrentText(str(self.configClass.APP_THEME_NAME))

        self.saveButton = QPushButton(text="save (needs app reopen)")
        self.saveButton.clicked.connect(self.saveData)

        self.settingsWindowBaseLayout.addWidget(QLabel(text="window width"))
        self.settingsWindowBaseLayout.addWidget(self.windowWidth)
        self.settingsWindowBaseLayout.addWidget(QLabel(text="window height"))
        self.settingsWindowBaseLayout.addWidget(self.windowHeight)
        self.settingsWindowBaseLayout.addWidget(QLabel(text="text size"))
        self.settingsWindowBaseLayout.addWidget(self.textSizeField)
        self.settingsWindowBaseLayout.addWidget(QLabel(text="font name"))
        self.settingsWindowBaseLayout.addWidget(self.fontType)
        self.settingsWindowBaseLayout.addWidget(QLabel(text="app style"))
        self.settingsWindowBaseLayout.addWidget(self.appStyle)
        self.settingsWindowBaseLayout.addWidget(QLabel(text="app theme"))
        self.settingsWindowBaseLayout.addWidget(self.appTheme)
        self.settingsWindowBaseLayout.addWidget(self.saveButton)

        self.setLayout(self.settingsWindowBaseLayout)

    def saveData(self):
        self.configClass.TEXT_SIZE = int(self.textSizeField.text())
        self.configClass.FONT_NAME = self.fontType.currentText()
        self.configClass.WINDOW_STYLE = self.appStyle.currentText()
        self.configClass.WINDOW_HEIGHT = int(self.windowHeight.text())
        self.configClass.WINDOW_WIDTH = int(self.windowWidth.text())
        self.configClass.APP_THEME = self.appTheme.currentText()
        self.configClass.save()
        self.close()
