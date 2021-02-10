class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0

    def get_speed_increase(self): #getter приватного значения speed
        return self.__speed

    def set_speed_increase(self):
        self.__speed += 5

    def set_speed_decrease(self):
        self.__speed -= 5

    def set_speed_stop(self):
        self.__speed = 0

    def set_speed_show(self):
        print(self.__speed)

    def set_speed_reversal(self):
        self.__speed *= (-1)

bmw = Car('bmw', 'A5', 2019)

bmw.set_speed_show()

bmw.set_speed_increase()
bmw.set_speed_increase() #увеличение на 10

bmw.set_speed_show()

bmw.set_speed_decrease() #уменьшение на 5

bmw.set_speed_show()

bmw.set_speed_stop() #сброс скорости на 0

bmw.set_speed_show()

bmw.set_speed_increase() #увеличение на 5

bmw.set_speed_show()

bmw.set_speed_reversal() #обратное значение скорости

bmw.set_speed_show()