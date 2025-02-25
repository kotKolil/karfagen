from PyQt5.Qt import *

class bottomNavigationPanel(object):
    def __init__(self, app):
        self.app = app

        self.bottomNavigationPanel = QWidget()
        self.navigationBoxLayout = QHBoxLayout()

        self.btn_prev = QPushButton(text="<")
        self.btn_prev.clicked.connect(self.prev_page)

        self.pageNumberLabel = QLabel(text=str(self.app.pageNumber))

        self.navigationSlider = QSlider(Qt.Horizontal)
        self.navigationSlider.setMinimum(1)
        self.navigationSlider.setMaximum(self.app.numOfPages)
        self.navigationSlider.sliderReleased.connect(self.renderPageFromSlider)

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
        self.goToPageField.editingFinished.connect(self.app.pageByNumber)

        self.navigationBoxLayout.addWidget(self.btn_prev)
        self.navigationBoxLayout.setAlignment(Qt.AlignCenter)
        self.navigationBoxLayout.addWidget(self.pageNumberLabel)
        self.navigationBoxLayout.addWidget(self.btn_next)
        self.navigationBoxLayout.addWidget(self.goToPageField)
        self.navigationBoxLayout.addWidget(self.navigationSlider)

        self.bottomNavigationPanel.setLayout(self.navigationBoxLayout)

    def renderPageFromSlider(self):
        pageNumber = self.navigationSlider.value()
        if pageNumber > 0 and pageNumber <= len(self.app.pages):
            self.goToPageField.setText(str(pageNumber))
            self.app.pageNumber = pageNumber
            self.app.render_page(pageNumber - 1)

    def prev_page(self):
        if self.app.pageNumber > 0 and self.app.Book:
            self.app.pageNumber -= 1
            self.app.render_page(self.app.pageNumber)

    def next_page(self):
        if self.app.pageNumber <= len(self.app.pages) and self.app.Book:
            self.app.pageNumber += 1
            self.app.render_page(self.app.pageNumber)