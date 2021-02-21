from random import randint
from time import sleep


def gen():
    while True:
        yield randint(0, 100)  # возвращает случайное значение в диапозоне от 0 до 100


g = gen()  # присваивает переменной функцию, делая ее генератором
for i in g:  # обращается к элементом генератора
    print(i)
    sleep(1)  # делает задержку в цикле
