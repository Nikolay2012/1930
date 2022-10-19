# паркування курсорів
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from modules.allButton import create_number_button, create_symbol_button, sort_button, show_buttons
from modules.allLayouts import main_VLayout
from modules.windows import*
#
create_number_button()
create_symbol_button()
sort_button()
show_buttons()
set_layouts()
 
win.show()
#
app.exec_()
