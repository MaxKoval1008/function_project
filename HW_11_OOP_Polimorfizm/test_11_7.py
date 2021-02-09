class Dog:
    def __init__(self, master):
        self.__master = master
    def get_master(self):
        return self.__master  #работает с приватным параметром

dog = Dog('Master')

dog.get_master()
print(dog._Dog__master)
