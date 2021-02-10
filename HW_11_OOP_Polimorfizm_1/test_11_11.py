class Dog:
    def __init__(self, name, age, weight):
        self.__name = name
        self.__age = age
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight


dog = Dog('Alex', 9, 25)

print(dog.name, dog.age, dog.weight)

dog.name = 'Leo'
dog.age = 1
dog.weight = 10

print(dog.name, dog.age, dog.weight)
