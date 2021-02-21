from operator import __abs__


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure(Point):
    pass


class Circle(Figure):
    def __init__(self, x_1, y_1, radius):
        super().__init__(x_1, y_1)
        self.radius = radius

    def per(self):
        per = self.radius * (2 * 3.1415)
        return per

    def square(self):
        square = 3.1415 * (self.radius**2)
        return square


class Triangle(Figure):
    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        self.x_3 = x_3
        self.y_3 = y_3
        self.side_1 = __abs__(((self.x_2 - self.x_1) ** 2 + (self.y_2 - self.y_1) ** 2) ** 0.5)
        self.side_2 = __abs__(((self.x_3 - self.x_2) ** 2 + (self.y_3 - self.y_2) ** 2) ** 0.5)
        self.side_3 = __abs__(((self.x_3 - self.x_1) ** 2 + (self.y_3 - self.y_1) ** 2) ** 0.5)

    def per(self):
        per = self.side_1 + self.side_2 + self.side_3
        return per

    def square(self):
        p = self.per()
        square = ((p*0.5)*((p*0.5) - self.side_1)*((p*0.5) - self.side_2)*((p*0.5) - self.side_3))**0.5
        return square


class Square(Figure):
    def __init__(self, x_1, y_1, x_2, y_2):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        self.side_1 = __abs__(self.x_1 - self.x_2)
        self.side_2 = __abs__(self.y_1 - self.y_2)
        self.side_3 = self.side_1
        self.side_4 = self.side_2

    def per(self):
        per = self.side_1 + self.side_2 + self.side_3 + self.side_4
        return per

    def square(self):
        square = self.side_1 * self.side_2
        return square


