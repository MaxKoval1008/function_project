class Dog:
    def __init__(self, master):
        self.__master = master
    def get_master(self):
        return self.__master  #работает с приватным параметром

dog = Dog('Jack')

print(dog.get_master())
