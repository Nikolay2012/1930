from modules.lists import list_input

def arithmeticsOperation():
    if list_input[1] == "+":
        number = int(list_input[0]) + int(list_input[2])
    elif list_input[1] == "-":
        number = int(list_input[0]) - int(list_input[2])
    return number