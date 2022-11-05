from modules.labels import label
from modules.lists import list_input, list_name_symbol, list_arithmetic_operation
from modules.arithmetics_operation import arithmeticsOperation
#
number = ""
def add_symbol(symbol):
    global number 
    if len(number) != 16:
        if symbol not in list_name_symbol:
            number += str(symbol)
            label.setText(number)
    if symbol in list_arithmetic_operation:
        list_input.append(number)
        number = ""
        list_input.append(symbol)
    if symbol == "=" and len(list_input) == 2:
        list_input.append(number)
        number = arithmeticsOperation()
        label.setText(str(number))
#
def add_minus():
    add_symbol("-")

def add_equal():
    add_symbol("=")
    
def add_plus():
    add_symbol("+")
#        
def add_one():
    add_symbol(1)
#
def add_two():
    add_symbol(2)
#
def add_three():
    add_symbol(3)
#
def add_four():
    add_symbol(4)
#
def add_five():
    add_symbol(5)
#
def add_six():
    add_symbol(6)
#
def add_seven():
    add_symbol(7)
#
def add_eight():
    add_symbol(8)
#
def add_nine():
    add_symbol(9)
#
def add_zero():
    add_symbol(0)
#
list_function = [
    add_zero,
    add_one, 
    add_two, 
    add_three, 
    add_four, 
    add_five, 
    add_six, 
    add_seven, 
    add_eight,
    add_nine
] 