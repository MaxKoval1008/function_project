from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def do_smth(self):
        print('I am a parent')


class B(A):
    def do_smth(self):
        print('I am a child')


b = B()

A.do_smth(1)

B.do_smth(1)
