from PyQt5.QtWidgets import(
    QApplication,
    QWidget
)
from modules.allLayouts import main_VLayout
#
app = QApplication([])
#
win = QWidget()
#
win.setWindowTitle("Calculator")
#
win.resize(300, 400)
#
def set_layouts():
    win.setLayout(main_VLayout)