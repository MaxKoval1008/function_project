class Math:
    def __init__(self, value_a: int, value_b: int):
        self.__value_a = value_a
        self.__value_b = value_b

    @property
    def value_a(self):
        return self.__value_a

    @value_a.setter
    def value_a(self, value):
        self.__value_a = value

    @property
    def value_b(self):
        return self.__value_b

    @value_b.setter
    def value_b(self, value):
        self.__value_b = value

    def addiction(self):
        return self.__value_a + self.__value_b

    def subtraction(self):
        return self.__value_a - self.__value_b

    def multiplication(self):
        return self.__value_a * self.__value_b

    def division(self):
        return self.__value_a / self.__value_b
