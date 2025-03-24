from src.GUI.panels.navigationTopPanel import *
from src.GUI.panels.bottomNavigationPanel import *
from src.GUI.widgets.textLabel import *

from PyQt5.Qt import *

import sys


class bookViewer(QApplication):
    def __init__(self, app_config=configParser()) -> None:
        super().__init__(sys.argv)
        self.setStyleSheet(app_config.APP_THEME_CSS)

        self.Book = None
        self.pages = []
        self.appConfig = app_config
        self.numOfPages = 1
        self.appStyle = self.appConfig.APP_THEME_CSS
        self.pageNumber = 0

        # creating and configuring bookViewer window
        self.content = QWidget()
        self.content.setWindowOpacity(self.appConfig.OPACITY_WINDOWS)
        self.content.setStyleSheet(app_config.APP_THEME_CSS)
        self.content.resize(0, 0)
        self.content.setFixedWidth(self.appConfig.WINDOW_WIDTH)
        self.content.setFixedHeight(self.appConfig.WINDOW_HEIGHT)
        self.content.setWindowIcon(QIcon("./assets/karfagen.png"))
        self.content.setWindowTitle(f"Karfagen Book reader")
        self.content.setStyleSheet(self.appStyle)
        self.appFont = QFont(self.appConfig.FONT_NAME, self.appConfig.TEXT_SIZE)
        self.setFont(self.appFont)
        self.text_height = QFontMetrics(self.appFont)

        self.layout = QVBoxLayout(self.content)

        self.layout.addWidget(navigationTopPanel(self))

        self.textLabel = textLabel(self).textLabel
        self.layout.addWidget(self.textLabel)

        self.navigationBottomPanel = bottomNavigationPanel(self)
        self.layout.addWidget(self.navigationBottomPanel)

        self.content.setLayout(self.layout)

    def start(self):
        self.content.show()
        self.exec_()

    def render_page(self, pageNumber):
        self.navigationBottomPanel.pageNumberLabel.setText(
            f"{str(pageNumber + 1)}/{len(self.pages)}")
        self.textLabel.setText("".join(self.pages[pageNumber]))

    def pageByNumber(self):
        pageNumber = int(self.navigationBottomPanel.goToPageField.text())
        if 0 < pageNumber <= len(self.pages):
            self.navigationBottomPanel.navigationSlider.setValue(pageNumber)
            self.pageNumber = pageNumber
            self.render_page(pageNumber - 1)

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.endswith(('.txt', '.epub', '.fb2')):
                print("cock")
        event.acceptProposedAction()


