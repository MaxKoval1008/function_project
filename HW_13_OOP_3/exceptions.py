class MyException(Exception):
    def __init__(self, message='Incorrect data'):
        super().__init__(message)


class MyTypeError(MyException):
    def __init__(self, message='Incorrect data type'):
        super().__init__(message)


class MyValueError(MyException):
    def __init__(self, message='Incorrect value for operation'):
        super().__init__(message)
