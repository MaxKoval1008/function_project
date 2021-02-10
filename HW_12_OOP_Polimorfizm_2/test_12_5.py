class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class B(A):
    def __init__(self, a, b, c, d, speices):  #добавляет новый аргумент
        super().__init__(a, b, c)
        self.d = d
        self.species = speices


a = A(2, 5, 10)

b = B(3, 6, 5, 4, 'aaa')

print(b.species)
