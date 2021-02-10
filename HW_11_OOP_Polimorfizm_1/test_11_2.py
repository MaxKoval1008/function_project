class Dog:
    def bark(self):  #метод класса
        print('Woof! Woof!')

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')


dog_1 = Dog()  #присвоение переменной класса

dog_1.bark()
dog_1.jump()
dog_1.run() #обращение к методу происходит таким образом, это возможно только если переменная относится к классу, в котором описан метод
