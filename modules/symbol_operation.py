from modules.labels import label
number = ""
def add_symbol(symbol):
    global number 
    if len(number) != 16:
        number += str(symbol)
        label.setText(number)
#        
def add_one():
    add_symbol(1)