class Dog:
    def __init__(self, name, weight, age):
        self.__name = name  #private
        self._age = age  #protected
        self.weight = weight  #public

dog = Dog('Bob', 8, 2.4)

# print(dog.__name) # так как этот тип данных защищен, система его не видел
print(dog._Dog__name)
print(dog._age)
print(dog.weight)
