class MyException(Exception):  # класс соббственной ошибки
    def __init__(self, message='AAA!!!'):
        super().__init__(message)


raise MyException
