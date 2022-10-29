from numpy import index_exp
from modules.lists import list_number_button
from modules.symbol_operation import *

for el in range(0,10):
    list_number_button[el].clicked.connect(list_function[el])