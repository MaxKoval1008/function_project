class A:
    def do_something(self):
        print('AA')

class B(A):
    def do_something(self):
        super().do_something() #вызывает родительский метод и переопределенная функция
        print('BB')

a = A()

a.do_something()

b = B()

b.do_something()