def convert_in_cm(input_value=0):
    return f'Convertation from inches to centimetres:\n {input_value} inches = {input_value * 2.54} cm'


def convert_cm_in(input_value=0):
    return f'Convertation from centimetres to inches:\n {input_value} cm = {input_value / 2.54} in'


def convert_mi_km(input_value=0):
    return f'Convertation from miles to kilometres:\n {input_value} mi = {input_value * 1, 60934} km'


def convert_km_mi(input_value=0):
    return f'Convertation from kilometres to miles:\n {input_value} km = {input_value * 1, 60934} mi'


def convert_lb_kg(input_value=0):
    return f'Convertation from pounds to kilograms:\n {input_value} lb = {input_value * 0, 453592} kg'


def convert_kg_lb(input_value=0):
    return f'Convertation from kilograms to pounds:\n {input_value} kg = {input_value / 0.453592} lb'


def convert_oz_g(input_value=0):
    return f'Convertation from oz to grams:\n {input_value} oz = {input_value * 28.3495} g'


def convert_g_oz(input_value=0):
    return f'Convertation from grams to oz:\n {input_value} g = {input_value / 28.3495} oz'


def convert_litres_gal(input_value=0):
    return f'Convertation from litres to gallons:\n {input_value} l = {input_value / 3.78541} gal'


def convert_gal_litres(input_value=0):
    return f'Convertation from gallons to litres:\n {input_value} gal = {input_value / 3.78541} l'


def convert_pt_litres(input_value=0):
    return f'Convertation from pints to litres:\n {input_value} pt = {input_value / 0.568261} l'


def convert_litres_pt(input_value=0):
    return f'Convertation from litres to pints:\n {input_value} l = {input_value / 0.568261} pt'


def menu_imitation():
    access_to_functions = {1: convert_in_cm,
                           2: convert_cm_in,
                           3: convert_mi_km,
                           4: convert_km_mi,
                           5: convert_lb_kg,
                           6: convert_kg_lb,
                           7: convert_oz_g,
                           8: convert_g_oz,
                           9: convert_gal_litres,
                           10: convert_litres_gal,
                           11: convert_pt_litres,
                           12: convert_litres_pt}
    print("Type number and press Enter for select menu item")

    while True:
        users_string = input("\n1 - Convert inches to centimetres\n"
                             "2 - Convert  centimetres to inches \n"
                             "3 - Convert miles to kilometres\n"
                             "4 - Convert kilometres to miles \n"
                             "5 - Convert pounds to kilograms\n"
                             "6 - Convert kilograms to pounds\n"
                             "7 - Convert oz to grams\n"
                             "8 - Convert grams to oz\n"
                             "9 - Convert gallons to litres\n"
                             "10 - Convert litres to gallons\n"
                             "11 - Convert pints to litres\n"
                             "12 - Convert litres to pints\n"
                             "0 - Exit\n"
                             )
        if users_string == 0:
            exit()
        else:
            print(access_to_functions[int(users_string)](int(input('Enter the value\n'))))


menu_imitation()
