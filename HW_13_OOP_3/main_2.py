import ui_func as ui
import classes as cl, exceptions


while True:
    try:

        arguments = ui.ui_menu()

        if arguments == 0:
            exit()
        if type(arguments) is not list:
            raise exceptions.MyException(arguments)
        calc = cl.Math(arguments[1], arguments[2])
        if arguments[0] == 1:
            print(f'{calc.value_a} + {calc.value_b} = {calc.addiction()}\n')
            continue
        if arguments[0] == 2:
            print(f'{calc.value_a} - {calc.value_b} = {calc.subtraction()}\n')
            continue
        if arguments[0] == 3:
            print(f'{calc.value_a} * {calc.value_b} = {calc.multiplication()}\n')
            continue
        if arguments[0] == 4:
            print(f'{calc.value_a} / {calc.value_b} = {calc.division()}\n')
            continue

    except exceptions.MyException as ex:
        print(ex)
