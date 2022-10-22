# паркування маркерів
from modules.windows import*
from modules.labels import showlabel
from modules.allButton import *
from modules.allLayouts import main_VLayout
from modules.clicked_connect import show_one
#
create_number_button()
create_symbol_button()
sort_button()
showlabel()
show_buttons()
set_layouts()

show_one()

win.show()
#
app.exec_()
   