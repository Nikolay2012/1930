from numpy import index_exp
from modules.lists import list_number_button, list_symbol_button
from modules.symbol_operation import *

for el in range(0,10):
    list_number_button[el].clicked.connect(list_function[el])

list_symbol_button[6].clicked.connect(add_plus)
list_symbol_button[5].clicked.connect(add_minus)
list_symbol_button[-2].clicked.connect(add_equal)