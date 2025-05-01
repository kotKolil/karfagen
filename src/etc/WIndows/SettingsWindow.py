from PyQt5.Qt import *
from src.etc.configParser import *
import os

class SettingsWindow(QWidget):

    def __init__(self, app):

        self.configClass = configParser()
        self.app = app

        super().__init__()

        self.setStyleSheet(self.configClass.APP_THEME)
        self.setWindowTitle(self.app.langPackage.lang.settings)
        self.setWindowIcon(QIcon("./assets/karfagen.png"))
        self.setFixedSize(600, 600)

        self.opacitySlider = QSlider(Qt.Horizontal)
        self.opacitySlider.setMinimum(1)
        self.opacitySlider.setMaximum(10)
        self.opacitySlider.setValue(int(self.configClass.OPACITY_WINDOWS * 10))
        self.opacitySlider.sliderReleased.connect(self.updateOpacity)

        self.opacityLabel = QLabel(text=f"{self.app.langPackage.lang.opacityIs} {self.configClass.OPACITY_WINDOWS}")

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

        self.langList = QComboBox()
        langList = []
        for i in os.listdir("./langPackages/"):
            langList.append(i.split(".")[0])
        self.langList.addItems(langList)

        self.saveButton = QPushButton(text=self.app.langPackage.lang.applySettingsButton)
        self.saveButton.clicked.connect(self.saveData)

        self.settingsWindowBaseLayout.addWidget(QLabel(text=self.app.langPackage.lang.windowWidth))
        self.settingsWindowBaseLayout.addWidget(self.windowWidth)
        self.settingsWindowBaseLayout.addWidget(QLabel(text= self.app.langPackage.lang.windowHeight))
        self.settingsWindowBaseLayout.addWidget(self.windowHeight)
        self.settingsWindowBaseLayout.addWidget(self.opacityLabel)
        self.settingsWindowBaseLayout.addWidget(self.opacitySlider)
        self.settingsWindowBaseLayout.addWidget(QLabel(text=self.app.langPackage.lang.fontSize))
        self.settingsWindowBaseLayout.addWidget(self.textSizeField)
        self.settingsWindowBaseLayout.addWidget(QLabel(text=self.app.langPackage.lang.fontType))
        self.settingsWindowBaseLayout.addWidget(self.fontType)
        self.settingsWindowBaseLayout.addWidget(QLabel(text=self.app.langPackage.lang.appStyle))
        self.settingsWindowBaseLayout.addWidget(self.appStyle)
        self.settingsWindowBaseLayout.addWidget(QLabel(text=self.app.langPackage.lang.langType))
        self.settingsWindowBaseLayout.addWidget(self.langList)
        self.settingsWindowBaseLayout.addWidget(QLabel(text=self.app.langPackage.lang.appTheme))
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
        self.configClass.OPACITY_WINDOWS = self.opacitySlider.value()  / 10
        self.configClass.langCode = self.langList.currentText()
        self.configClass.save()
        self.close()

    def updateOpacity(self):
        value = self.opacitySlider.value()
        self.opacityLabel.setText(f"{self.app.langPackage.lang.opacityIs} {value/10}")
