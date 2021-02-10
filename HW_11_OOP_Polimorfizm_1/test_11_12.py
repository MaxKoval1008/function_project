class Dog:
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

    def bark(self):
        print('Woof!')


class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('Run!')

    def jump(self, ):
        print('Jump!')

    def birthday(self):
        self.age += 1
        print(self.age)
        return self.age


    def sleep(self):
        print('Dream...')

    def meow(self):
        print('Meow!')


class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('Run!')

    def jump(self):
        print('Jump!')

    def birthday(self, age):
        self.age += 1
        print(age)
        return age

    def sleep(self):
        print('Dream...')

    def fly(self):
        print('Fly!')


sindi = Cat('Sindi', 3, 'master')

sindi.meow()
sindi.birthday()
