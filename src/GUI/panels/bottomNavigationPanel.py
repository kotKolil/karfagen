from PyQt5.Qt import *

class bottomNavigationPanel(QWidget):
    def __init__(self, app):
        super().__init__()
        
        self.app = app

        self.navigationBoxLayout = QVBoxLayout()

        self.navigationBoxLayout2 = QHBoxLayout()

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
        self.goToPageField.setPlaceholderText(self.app.langPackage.lang.pageByNumberPlaceholder)
        self.goToPageField.setStyleSheet("""
            QLineEdit {
                border: 0px black solid;
                background-color: #bbbbbb;
                color: #000000;
            }
        """)
        self.goToPageField.editingFinished.connect(self.app.pageByNumber)

        self.navigationBoxLayout2.addWidget(self.btn_prev)
        self.navigationBoxLayout2.setAlignment(Qt.AlignCenter)
        self.navigationBoxLayout2.addWidget(self.pageNumberLabel)
        self.navigationBoxLayout2.addWidget(self.btn_next)
        self.navigationBoxLayout2.addWidget(self.goToPageField)

        self.fooBazz = QWidget()
        self.fooBazz.setLayout(self.navigationBoxLayout2)
        self.navigationBoxLayout.addWidget(self.navigationSlider)
        self.navigationBoxLayout.addWidget(self.fooBazz)

        self.setLayout(self.navigationBoxLayout)

    def renderPageFromSlider(self):
        pageNumber = self.navigationSlider.value()
        if pageNumber > 0 and pageNumber <= len(self.app.pages):
            self.goToPageField.setText(str(pageNumber))
            self.app.pageNumber = pageNumber
            self.app.render_page(pageNumber - 1)

    def prev_page(self):
        if self.app.pageNumber > 0 and self.app.Book:
            self.app.pageNumber -= 1
            self.navigationSlider.setValue(self.app.pageNumber)
            self.app.render_page(self.app.pageNumber)

    def next_page(self):
        try:
            if self.app.pageNumber <= len(self.app.pages) - 2 and self.app.Book:
                self.app.pageNumber += 1
                self.navigationSlider.setValue(self.app.pageNumber)
                self.app.render_page(self.app.pageNumber)
        except:
            pass