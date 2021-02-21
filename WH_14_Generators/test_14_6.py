from time import sleep
from random import randint


def create_generator(a, b, n):
    while True:
        yield randint(a, b)
        a += n
        b += n


my_list = create_generator(1, 10, 10)
while True:
    print(next(my_list))
    sleep(1)

# my_list = create_generator(1, 10, 10)  # как альтернативный вариант решения
# print(my_list)
# for i in my_list:
#     print(i)
#     sleep(1)