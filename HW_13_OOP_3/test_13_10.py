from abc import ABC, abstractmethod


class MyInterface(ABC):
    @abstractmethod
    def do_a(self, arg1):
        raise NotImplemented

    @abstractmethod
    def do_b(self, arg1, arg2):
        raise NotImplemented


class MyClass(MyInterface):
    def do_a(self, arg1):
        print(arg1)

    def do_b(self, arg1, arg2):
        print(arg1, arg2)
