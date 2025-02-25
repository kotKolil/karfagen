from PyQt5.Qt import *
from src.configParser import *


class settingsWindow(object):

    def __init__(self):
        self.configClass = configParser()

        self.settingsWindowBase = QWidget()
        self.settingsWindowBase.setStyleSheet(self.configClass.APP_THEME)
        self.settingsWindowBase.setWindowTitle("settings")
        self.settingsWindowBase.setWindowIcon(QIcon("./media/karfagen.png"))
        self.settingsWindowBase.setFixedSize(300, 300)

        self.settingsWindowBaseLayout = QVBoxLayout()

        self.textSizeField = QLineEdit()
        self.textSizeField.setValidator(QIntValidator())
        self.textSizeField.setText(str(self.configClass.TEXT_SIZE))

        self.fontType = QComboBox()
        self.fontType.addItems(QFontDatabase().families())
        self.fontType.setCurrentText(str(self.configClass.FONT_NAME))

        self.appStyle = QComboBox()
        self.appStyle.addItems(QStyleFactory.keys())
        self.appStyle.setCurrentText(str(self.configClass.WINDOW_STYLE))

        self.appTheme = QComboBox()
        self.appTheme.addItems(["white", "dark", "console"])
        self.appTheme.setCurrentText(str(self.configClass.APP_THEME))

        self.saveButton = QPushButton(text="save (needs app reopen)")
        self.saveButton.clicked.connect(self.saveData)

        self.settingsWindowBaseLayout.addWidget(QLabel(text="text size"))
        self.settingsWindowBaseLayout.addWidget(self.textSizeField)
        self.settingsWindowBaseLayout.addWidget(QLabel(text="font name"))
        self.settingsWindowBaseLayout.addWidget(self.fontType)
        self.settingsWindowBaseLayout.addWidget(QLabel(text="app style"))
        self.settingsWindowBaseLayout.addWidget(self.appStyle)
        self.settingsWindowBaseLayout.addWidget(QLabel(text="app theme"))
        self.settingsWindowBaseLayout.addWidget(self.appTheme)
        self.settingsWindowBaseLayout.addWidget(self.saveButton)

        self.settingsWindowBase.setLayout(self.settingsWindowBaseLayout)

    def start(self):
        self.settingsWindowBase.show()

    def saveData(self):
        self.configClass.TEXT_SIZE = int(self.textSizeField.text())
        self.configClass.FONT_NAME = self.fontType.currentText()
        self.configClass.WINDOW_STYLE = self.appStyle.currentText()
        self.configClass.APP_THEME = self.appTheme.currentText()
        self.configClass.save()
        self.settingsWindowBase.close()