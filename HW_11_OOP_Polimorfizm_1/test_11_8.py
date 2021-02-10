class Dog:
    def __init__(self, master):
        self.__master = master
    def get_master(self):  #функция которая получает доступ к приватным аргументам
        return self.__master
    def set_master(self, master):  #функция которая позволяет установить значение приватного аргумента
        self.__master = master

dog = Dog('Alex')
print(dog.get_master())
dog.set_master('Pavel')
print(dog.get_master())
