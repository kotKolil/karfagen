from src.Book import *
from src.configParser import *

from src.app.navigationTopPanel import *
from src.app.bottomNavigationPanel import *
from src.app.textLabel import *

from PyQt5.Qt import *

import sys


class bookViewer(object):
    def __init__(self, app=QApplication(sys.argv), appConfig = configParser()) -> None:

        self.app = app
        self.app.setStyle(appConfig.WINDOW_STYLE)

        self.Book = None
        self.pages = []
        self.appConfig = appConfig
        self.numOfPages = 1
        self.appStyle = self.appConfig.APP_THEME
        self.pageNumber = 0

        # creating and configuring bookViewer window
        self.content = QWidget()
        self.content.setFixedSize(500, 500)
        self.content.setWindowIcon(QIcon("./media/karfagen.png"))
        self.content.setWindowTitle(f"Karfagen Book Viewer")
        self.content.setStyleSheet(self.appStyle)
        self.appFont = QFont(self.appConfig.FONT_NAME, self.appConfig.TEXT_SIZE)
        self.app.setFont(self.appFont)
        self.text_height = QFontMetrics(self.appFont)

        self.layout = QVBoxLayout(self.content)

        self.navigationTopPanel = navigationTopPanel(self)
        self.layout.addWidget(self.navigationTopPanel.navigationTopPanel)

        self.textLabel = textLabel(self)
        self.layout.addWidget(self.textLabel.textLabel)

        self.navigationBottomPanel = bottomNavigationPanel(self)
        self.layout.addWidget(self.navigationBottomPanel.bottomNavigationPanel)

        self.content.setLayout(self.layout)





    def start(self):
        self.content.show()
        self.app.exec_()

    def render_page(self, pageNumber):
        try:
            self.pageNumberLabel.setText(f"{str(pageNumber + 1)}/{len(self.pages)}")
            self.textLabel.setText("".join(self.pages[pageNumber]))
        except Exception as e:
            self.show_messagebox(str(e))

    def pageByNumber(self):
        pageNumber = int(self.goToPageField.text())
        if pageNumber > 0 and pageNumber <= len(self.pages):
            self.navigationSlider.setValue(pageNumber)
            self.pageNumber = pageNumber
            self.render_page(pageNumber - 1)
