class Pet:
    __counter = 0

    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        Pet.__counter += 1 #функция подсчета Pet

    def change_weight(self, weigth):
        self.weight = weigth

    def change_height(self, heigth):
        self.height = heigth

    def jump(self, jump: float):
        print(f'Jump {jump} meters')

    def voice(self):
        pass

    def get_counter(self): #метод вывода приватного значения counter
        return print(self.__counter)


class Dog(Pet):

    def run(self):
        print('Run!')

    def birthday(self):
        self.age += 1
        print(self.age)

    def sleep(self):
        print('Dream...')

    def voice(self):
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

    def voice(self):
        print('Meow!')


class Parrot(Pet):
    def __init__(self, name, height, weight, age, species):
        super().__init__(name, height, weight, age)  # добавление нового атрибута через super
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

    def voice(self):
        print('Chic-Chirick!')

    def change_weight(self, *args):
        if args == ():
            self.weight += 0.5
        else:
            self.weight += int(args[0])


hasky = Dog('Jack', 97, 23, 8)

british = Cat('Snow', 44, 11, 2)

pirat = Parrot('Pirat', 14, 1, 3, 'badge')

Pet.get_counter(Pet)


