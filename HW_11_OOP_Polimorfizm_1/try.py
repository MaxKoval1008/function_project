class Car:
    def __init__(self, brand, year):
        self.__brand = brand
        self.__year = year
        self.__speed = 0

    def get_speed_increase(self):
        return self.__speed

    def set_speed_increase(self):
        self.__speed += 5


bmw = Car('BMW', 2014)
print(bmw.get_speed_increase())
bmw.set_speed_increase()
bmw.set_speed_increase()
print(bmw.get_speed_increase())

