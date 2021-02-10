class Material:
    def crash(self):
        print('Boom!')

    def put(self):
        print('Put!')


class Brick(Material):
    def __init__(self, weight, cost, strenght):
        self.__weight = weight
        self.__cost = cost
        self.__strenght = strenght

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @property
    def strenght(self):
        return self.__strenght

    @strenght.setter
    def strenght(self, strenght):
        self.__strenght = strenght


class Sandstone(Material):
    def __init__(self, weight, cost, strenght):
        self.__weight = weight
        self.__cost = cost
        self.__strenght = strenght

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @property
    def strenght(self):
        return self.__strenght

    @strenght.setter
    def strenght(self, strenght):
        self.__strenght = strenght


class Bar(Material):
    def __init__(self, weight, cost, strenght):
        self.__weight = weight
        self.__cost = cost
        self.__strenght = strenght

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @property
    def strenght(self):
        return self.__strenght

    @strenght.setter
    def strenght(self, strenght):
        self.__strenght = strenght


class Foam_concrete_block(Material):
    def __init__(self, weight, cost, strenght):
        self.__weight = weight
        self.__cost = cost
        self.__strenght = strenght

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @property
    def strenght(self):
        return self.__strenght

    @strenght.setter
    def strenght(self, strenght):
        self.__strenght = strenght


class Stone(Material):
    def __init__(self, weight, cost, strenght):
        self.__weight = weight
        self.__cost = cost
        self.__strenght = strenght

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @property
    def strenght(self):
        return self.__strenght

    @strenght.setter
    def strenght(self, strenght):
        self.__strenght = strenght


brick = Brick(1.0, 8, 0.7)
brick.crash()
brick.put()
print(brick.weight, brick.cost, brick.strenght)

brick.weight = 0.9
brick.cost = 7.5
brick.strenght = 0.65

print(brick.weight, brick.cost, brick.strenght)

brick = Brick(1.0, 8, 0.7)
brick.crash()
brick.put()
print(brick.weight, brick.cost, brick.strenght)

brick.weight = 0.9
brick.cost = 7.5
brick.strenght = 0.65

print(brick.weight, brick.cost, brick.strenght)

stone = Stone(1.2, 10, 1)
stone.crash()
stone.put()
print(stone.weight, stone.cost, stone.strenght)

stone.weight = 2
stone.cost = 8
stone.strenght = 0.9

print(stone.weight, stone.cost, stone.strenght)
