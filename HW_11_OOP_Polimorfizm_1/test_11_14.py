class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('Run!')

    def jump(self):
        print('Jump!')

    def birthday(self):
        self.age += 1
        print(self.age)

    def sleep(self):
        print('Dream...')


class Dog(Pet):
    # def __init__(self, name, age, master):
    #     self.name = name
    #     self.age = age
    #     self.master = master

    def bark(self):
        print('Woof!')


class Cat(Pet):
    # def __init__(self, name, age, master):
    #     self.name = name
    #     self.age = age
    #     self.master = master

    def meow(self):
        print('Meow!')


class Parrot(Pet):
    # def __init__(self, name, age, master):
    #     self.name = name
    #     self.age = age
    #     self.master = master

    def fly(self):
        print('Fly!')


skippy = Cat('Skippy', 3, 'masrer')
holly = Dog('Holly', 7, 'master')
pirat = Parrot('Pirat', 1, 'master')

skippy.meow()
skippy.birthday()

holly.bark()
holly.birthday()

pirat.fly()
pirat.birthday()
