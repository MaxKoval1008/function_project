class Parent:
    def print_world(self):
        print('world')


class Child(Parent):  #перенимает методы родительского конструктораW
    def print_hello(self):
        print('hello')


a = Child()

a.print_hello()
a.print_world()