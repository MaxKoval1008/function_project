class A:
    def do_something(self):  #определение основного метода
        print('AA')


class B(A):
    def do_something(self):  #переопределение метода - полиморфизм (перегрузка оператора)
        print('BB')


a = A()

a.do_something()

b = B()

b.do_something()

c = B()

c.do_something()  #для объектов класса В тот же метод будет переприсвоен

a.do_something()  #для объектов класса А метод сохраняется изначальный
