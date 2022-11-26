from modules.lists import *
#
width = 56
height = 56
font_size = 28
color_text = (225,225,225)
bg_color = (155,155,155)
#
# def reSize(width, height, object):
    # object.setMaximumWidth(width)
    # object.setMaximumHeight(height)
#
# for el in range(1, 10): 
    # reSize(size, size, list_number_button[el])

# for el in list_symbol_button:
    # reSize(size, size, el)

# reSize(110, size, list_number_button[0])

def button_style():
    for el in range(3, 8):
        list_symbol_button[el].setStyleSheet(
            f'''
                background-color: orange;
                color: rgb{color_text};
                font-size: {font_size}px;
                max-width: {width}px;
                max-height: {height}px;
            '''
        )
    
    for el in range(0,3):
        list_symbol_button[el].setStyleSheet(
            f'''
                background-color: dimgrey;
                color: rgb{color_text};
                font-size: {font_size}px;
                max-width: {width}px;
                max-height: {height}px;
            '''
        )
    
    for el in range(1, len(list_number_button)):
        list_number_button[el].setStyleSheet(
            f'''
                background-color: rgb{bg_color};
                color: rgb{color_text};
                font-size: {font_size}px;
                max-width: {width}px;
                max-height: {height}px;
            '''
        )
    
    list_symbol_button[-1].setStyleSheet(
        f'''
            background-color: rgb{bg_color};
            color: rgb{color_text};
            font-size: {font_size}px;
            max-width: {width}px;
            max-height: {height}px;
        '''
        )

    list_number_button[0].setStyleSheet(
        f'''
            max-width: 115px; 
            max-height: {height}px;
            background-color: rgb{bg_color}; 
            color: rgb{color_text};
            font-size: {font_size}px;
        '''
    )

    
button_style()