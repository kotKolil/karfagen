from src.GUI.panels.navigationTopPanel import *
from src.GUI.panels.bottomNavigationPanel import *
from src.GUI.widgets.textLabel import *

from PyQt5.Qt import *

import sys


class bookViewer(QApplication):
    def __init__(self, appConfig=configParser()) -> None:
        super().__init__(sys.argv)
        self.setStyleSheet(appConfig.APP_THEME_CSS)

        self.Book = None
        self.pages = []
        self.appConfig = appConfig
        self.numOfPages = 1
        self.appStyle = self.appConfig.APP_THEME_СSS
        self.pageNumber = 0

        # creating and configuring bookViewer window
        self.content = QWidget()
        self.content.setAcceptDrops(True)
        self.content.setAttribute(Qt.WA_AcceptTouchEvents, True)
        self.content.installEventFilter(self)
        self.content.setMouseTracking(True)
        self.content.setWindowOpacity(self.appConfig.OPACITY_WINDOWS)
        self.content.setStyle(appConfig.APP_THEME_СSS)
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

    def closeEvent(self, event):
        print("cock")
        for filename in os.listdir("./images"):
            file_path = os.path.join("./images", filename)
            # Check if it's a file
            if os.path.isfile(file_path):
                os.remove(file_path)
        event.accept()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.endswith(('.txt', '.epub', '.fb2')):
                print("cock")
        event.acceptProposedAction()


