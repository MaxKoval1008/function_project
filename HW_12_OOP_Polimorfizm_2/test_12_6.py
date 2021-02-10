class Pet:
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

    def change_weight(self, weigth):
        self.weight = weigth

    def change_height(self, heigth):
        self.height = heigth

    def jump(self, jump: float):
        print(f'Jump {jump} meters')


class Dog(Pet):

    def run(self):
        print('Run!')

    def birthday(self):
        self.age += 1
        print(self.age)

    def sleep(self):
        print('Dream...')

    def bark(self):
        print('Woof!')

    def jump(self, jump):
        if jump > 0.5:
            print(f'Dogs connot jump so hight')
        else:
            super().jump(jump)


class Cat(Pet):

    def run(self):
        print('Run!')

    def jump(self, jump):
        if jump > 2:
            print(f'Cats connot jump so hight')
        else:
            super().jump(jump)

    def birthday(self):
        self.age += 1
        print(self.age)
        return self.age


    def sleep(self):
        print('Dream...')

    def meow(self):
        print('Meow!')


class Parrot(Pet):
    def __init__(self, name, height, weight, age, species):
        super().__init__(name, height, weight, age) #добавление нового атрибута через super
        self.species = species

    def run(self):
        print('Run!')

    def jump(self, jump):
        if jump > 0.05:
            print(f'Parrot connot jump so hight')
        else:
            super().jump(jump)

    def birthday(self, age):
        self.age += 1
        print(age)
        return age

    def sleep(self):
        print('Dream...')

    def fly(self):
        print('Fly!')

    def change_weight(self, *args):
        if args == ():
            self.weight += 0.5
        else:
            self.weight += int(args[0])


# dog = Dog('Bob', 100, 40, 10)
#
# dog.jump(0.8)
#
# cat = Cat('Bob', 100, 40, 10)
#
# cat.jump(0.8)
#
# parrot = Parrot('Bob', 100, 40, 2, 'aaaa')
#
# parrot.jump(0.8)
#
# print(parrot.species)
p = Parrot('Bob', 1, 2, 3, 'aaa')

print(p.species)