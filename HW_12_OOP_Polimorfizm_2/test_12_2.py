class Pet:
    def __init__(self, name: str, height: int, weight: int):
        self.name = name
        self.height = height
        self.weight = weight

    def change_weight(self, weigth):
        self.weight = weigth

    def change_height(self, heigth):
        self.height = heigth


class Parrot(Pet):
    # def change_weigth(self):
    #     self.weight += 0.05
    #     return self.weight

    def change_weight(self, *args):
        if args == ():
            self.weight += 0.5
        else:
            self.weight += int(args[0])


budgerigar = Parrot('Bob', 10, 3)

budgerigar.change_weight(2)

print(budgerigar.weight)

budgerigar.change_weight()

print(budgerigar.weight)
