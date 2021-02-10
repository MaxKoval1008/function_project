class Dog:
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

    def bark(self):  #метод класса
        print('Woof! Woof!')

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def change_height(self, height):  #метод переписывающий объявленный атрибут
        self.height = height


dog_1 = Dog('Jack', 102, 43, 9)  #присвоение переменной класса

dog_1.bark()
dog_1.jump()
dog_1.run() #обращение к методу происходит таким образом, это возможно только если переменная относится к классу, в котором описан метод
print(dog_1.name, dog_1.height, dog_1.weight, dog_1.age)

dog_1.change_height(115)
print(dog_1.name, dog_1.height, dog_1.weight, dog_1.age)
