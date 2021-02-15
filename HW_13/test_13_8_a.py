class MyExection_1(Exception):
    def __init__(self, message='Sence wrong'):
        super().__init__(message)


class MyExection_2(Exception):
    def __init__(self, message='Sence zero'):
        super().__init__(message)


class Book:
    def __init__(self, pages, year, writer, price):
        try:  # осуществление проверки на нижеописанные условия
            self.pages = int(pages)
        except ValueError as err:  # при срабатывании ошибки типа ValueError программа выдает нижеприведенный текст
            print('Value pages must be integer, not string')
        if self.pages == -10:  # при срабатывании данного условия программа экстренно прерывается с указанной ошибкой
            raise MyExection_1
        if self.pages == 0:
            raise MyExection_2
        else:
            print('Not Wrongs')

        try:
            self.year = int(year)
        except ValueError as err:
            print('Value year must be integer, not string')
        except Exception as err:
            print(f'SOMETHING WRONG - {err}')
        else:
            print('Not Wrongs')

        try:
            self.writer = str(writer)
        except ValueError as err:
            print('Value writer must be string, not integer')
        except Exception as err:
            print(f'SOMETHING WRONG - {err}')
        else:
            print('Not Wrongs')

        try:
            self.price = int(price)
        except ValueError as err:
            print('Value price must be integer, not string')
        except Exception as err:
            print(f'SOMETHING WRONG - {err}')
        else:
            print('Not Wrongs')


a = Book('sda', 2002, 'name', 100)


