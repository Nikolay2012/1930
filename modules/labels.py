from ctypes import alignment

from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from modules.allLayouts import main_VLayout
from modules.fonts import font1
#
label = QLabel("_")
#
label.setFont(font1)
#
def showlabel():
    main_VLayout.addWidget(label, alignment= Qt.AlignRight)