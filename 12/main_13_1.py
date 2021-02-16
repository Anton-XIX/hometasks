import ui_func as ui
import func, exceptions



while True:
    try:
        arguments = ui.ui_menu()
        if arguments == 0:
            exit()
        if type(arguments) is not list:
            raise exceptions.MyException(arguments)
        if arguments[0] == 1:
            print(f'{arguments[1]} + {arguments[2]} = {func.summ(arguments[1], arguments[2])}\n')
            continue
        if arguments[0] == 2:
            print(f'{arguments[1]} - {arguments[2]} = {func.subtraction(arguments[1], arguments[2])}\n')
            continue
        if arguments[0] == 3:
            print(f'{arguments[1]} * {arguments[2]} = {func.multiply(arguments[1], arguments[2])}\n')
            continue
        if arguments[0] == 4:
            print(f'{arguments[1]} / {arguments[2]} = {func.division(arguments[1], arguments[2])}\n')
            continue
        if arguments[0] == 0:
            exit()
    except exceptions.MyException as me:
        print(me)


