from src.Book import *
from src.configParser import *
from src.settingsWindow import *

from PyQt5.Qt import *

import sys


class BookViewer(object):
    def __init__(self, app=QApplication(sys.argv), appConfig = configParser()) -> None:

        self.app = app
        self.app.setStyle(appConfig.WINDOW_STYLE)
        self.Book = None
        self.pages = []
        self.appConfig = appConfig
        self.numOfPages = 1
        self.appStyle = self.appConfig.APP_THEME

        # creating and configuring BookViewer window
        self.content = QWidget()
        self.content.setFixedSize(500, 500)
        self.content.setWindowIcon(QIcon("./media/karfagen.png"))
        self.content.setWindowTitle(f"Karfagen Book Viewer")
        self.content.setStyleSheet(self.appStyle)
        self.text_font = QFont(self.appConfig.FONT_NAME, self.appConfig.TEXT_SIZE)
        self.text_height = QFontMetrics(self.text_font)

        self.layout = QVBoxLayout(self.content)

        self.pageNumber = 0

        self.textLabel = QLabel()
        self.textLabel.setWordWrap(1)
        self.textLabel.setFixedWidth(400)
        self.textLabel.setFixedHeight(400)

        self.navigationBox = QGroupBox()
        self.navigationBox.setStyleSheet("""
        QGroupBox {
            border: 0px black solid;
        }
        """)

        #creating navigation panel
        self.navigationTopPanel = QWidget()
        self.navigationTopPanelLayout = QHBoxLayout()
        self.navigationTopPanel.setLayout(self.navigationTopPanelLayout)

        self.openFile = QPushButton(text = "open file")
        self.openFile.clicked.connect(self.openFileFunc)
        self.openFile.setFixedWidth(70)

        self.settingsButton = QPushButton(text = "settings")
        self.settingsButton.clicked.connect(self.settingsWindow)

        self.layout.addWidget(self.navigationTopPanel)

        self.navigationTopPanelLayout.addWidget(self.openFile)
        self.navigationTopPanelLayout.addWidget(self.settingsButton)
        self.navigationTopPanelLayout.setAlignment(Qt.AlignLeft)

        self.navigationSlider = QSlider(Qt.Horizontal)
        self.navigationSlider.setMinimum(1)
        self.navigationSlider.setMaximum(self.numOfPages)
        self.navigationSlider.sliderReleased.connect(self.renderPageFromSlider)

        #creating elements for navigation in Book
        self.navigationBoxLayout = QHBoxLayout()

        self.btn_prev = QPushButton(text="<")
        self.btn_prev.clicked.connect(self.prev_page)

        self.pageNumberLabel = QLabel(text=str(self.pageNumber))

        self.btn_next = QPushButton(text=">")
        self.btn_next.clicked.connect(self.next_page)

        self.goToPageField = QLineEdit()
        self.goToPageField.setValidator(QIntValidator())
        self.goToPageField.setPlaceholderText("Enter number of page to go")
        self.goToPageField.setStyleSheet("""
            QLineEdit {
                border: 0px black solid;
                background-color: #bbbbbb;
                color: #000000;
            }
        """)
        self.goToPageField.editingFinished.connect(self.pageByNumber)

        self.navigationBoxLayout.addWidget(self.btn_prev)
        self.navigationBoxLayout.setAlignment(Qt.AlignCenter)
        self.navigationBoxLayout.addWidget(self.pageNumberLabel)
        self.navigationBoxLayout.addWidget(self.btn_next)
        self.navigationBoxLayout.addWidget(self.goToPageField)
        self.navigationBoxLayout.addWidget(self.navigationSlider)

        self.navigationBox.setLayout(self.navigationBoxLayout)

        self.layout.addWidget(self.textLabel)
        self.layout.addStretch()
        self.layout.addWidget(self.navigationBox)

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
            self.pageNumber = pageNumber
            self.render_page(pageNumber - 1)

    def renderPageFromSlider(self):
        pageNumber = self.navigationSlider.value()
        if pageNumber > 0 and pageNumber <= len(self.pages):
            self.pageNumber = pageNumber
            self.render_page(pageNumber - 1)

    def prev_page(self):
        if self.pageNumber > 0 and self.Book:
            self.pageNumber -= 1
            self.render_page(self.pageNumber)

    def next_page(self):
        if self.pageNumber <= len(self.pages) and self.Book:
            self.pageNumber += 1
            print(self.pageNumber)
            self.render_page(self.pageNumber)

    def parseBookData(self):
        """
        Parses raw book data into pages, handling paragraph wrapping and page breaks.

        Returns:
            A list of pages, where each page is a list of strings (paragraphs/lines).
        """

        pages= []
        page = []
        current_text_height = 0
        font_metrics = QFontMetrics(QFont(self.appConfig.FONT_NAME, self.appConfig.TEXT_SIZE))

        for paragraph in self.Book.text_data:
            # Split paragraph into lines that fit
            lines = self.split_paragraph_into_lines(paragraph, font_metrics, self.textLabel.width())
            for line in lines:
                line_height = font_metrics.height()  # Use actual line height

                if current_text_height + line_height <= self.textLabel.height():
                    page.append(line + "<br>")
                    current_text_height += line_height
                else:
                    pages.append(page)
                    page = [line]
                    current_text_height = line_height  # Reset height to the current line's height

        # Add the last page if it's not empty
        if page:
            pages.append(page)

        return pages

    def split_paragraph_into_lines(self, paragraph: str, font_metrics: QFontMetrics, max_width: int):
        """
        Splits a paragraph into lines that fit within the maximum width, handling word wrapping.

        Args:
            paragraph: The paragraph to split.
            font_metrics: QFontMetrics object.
            max_width: The maximum width for a line.

        Returns:
            A list of strings, where each string is a line.
        """

        if font_metrics.horizontalAdvance(paragraph) >= self.textLabel.width():

            words = paragraph.split()
            lines = []
            current_line = ""

            for word in words:
                test_line = current_line + word + " "  # Add word and a space to test
                if font_metrics.horizontalAdvance(test_line) <= max_width:
                    current_line = test_line
                else:
                    if current_line:  # Add the current line if it's not empty
                        newString = ""
                        for i in range(len(current_line)):
                            newString += current_line[i]
                            if font_metrics.horizontalAdvance(newString) == max_width:
                                break
                    lines.append(newString)
                    current_line = word + " " + current_line[i:len(current_line)]  # Start a new line with the current word

            if current_line:  # Add the last line
                lines.append(current_line.strip())
            return lines

        else:
            return [paragraph]

    def openFileFunc(self):
        options = QFileDialog.Options()

        # Get the file names from the dialog
        files, _ = QFileDialog.getOpenFileNames(self.content,
                                                 "Select Fiction Book Files",
                                                 "",
                                                 "Fiction Book 2 (*.fb2);;All Files (*)",
                                                 options=options)
        if files:
            self.Book = Book(files[0])
            self.Book.parse()

            self.content.setWindowTitle(self.Book.title + " " + self.Book.author + " " + "Karfagen Book Viewer")
            self.pages = self.parseBookData()
            self.numOfPages = len(self.pages)
            self.render_page(self.pageNumber)
            self.navigationSlider.setMaximum(self.numOfPages)


    def settingsWindow(self):
        self.settingsWindowBase = settingsWindow()
        self.settingsWindowBase.start()