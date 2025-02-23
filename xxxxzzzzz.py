from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
layout = QHBoxLayout()

navigationSlider = QSlider()
navigationSlider.setMaximum(1)

navigationSlider.setOrientation(Qt.Horizontal)

layout.addWidget(navigationSlider)

window.setLayout(layout)

window.show()

sys.exit(app.exec_())
