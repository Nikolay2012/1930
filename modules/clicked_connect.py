from modules.lists import list_number_button
from modules.symbol_operation import add_one

def show_one():
    list_number_button[1].clicked.connect(add_one)