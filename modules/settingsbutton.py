from modules.lists import *
#
size = 50
#
def reSize(width, height, object):
    object.setMaximumWidth(width)
    object.setMaximumHeight(height)
#
for el in range(1, 10): 
    reSize(size, size, list_number_button[el])
#
for el in list_symbol_button:
    reSize(size, size, el)
#
reSize(110, size, list_number_button[0])