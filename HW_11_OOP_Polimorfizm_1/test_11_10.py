class Dog:
    def __init__(self, master):
        self.__master = master
    @property  #декоратор getter, выполняет тоже самое что и функция get_master
    def master(self):
        return self.__master
    @master.setter  #декоратор setter, выполняет тоже самое что и функция set_master
    def master(self, master):
        if len(master) < 5:
            self.__master = master


dog = Dog('Alex')
dog.master = 'Jonatan'
print(dog.master)
