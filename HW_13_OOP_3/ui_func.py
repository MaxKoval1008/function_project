import exceptions

menu = {'addition': 1, 'subtraction': 2, 'multiply': 3, 'division': 4, 'exit': 0}


def ui_menu():
    print('Choose number of operation:')
    for key, value in menu.items():
        print(f'{key} - {value}')
    try:
        choice = input('\nEnter: ')
        if not choice.isdigit():
            raise exceptions.MyTypeError('Error type of choice\n')
        else:
            choice = int(choice)
            if choice == 0:
                return choice
        if choice > 4:
            raise exceptions.MyValueError('Incorrect menu item\n')

        value_a = input('Type first argument\n')
        value_b = input('Type second argument\n')
        if not value_a.isdigit() or not value_b.isdigit():
            raise exceptions.MyTypeError('Incorrect type of arguments\n')
        else:
            return [choice, int(value_a), int(value_b)]

    except exceptions.MyValueError as mve:
        return mve

    except exceptions.MyTypeError as mte:
        return mte

    except Exception('Something was wrong') as e:
        return e
