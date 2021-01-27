print('Hello world!')


def my_func(a, b):
    summ = a + b
    print(f'{a} + {b} = {summ}')
    return summ


my_func(4, 5)
my_func(6, 7)
my_func(8, 0)

a = my_func(4, 3)
print(a)
