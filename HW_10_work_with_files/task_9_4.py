def my_decorator(func):
    def do_func(my_func):
        my_func = [i for i in my_func[::-1]]
        print(my_func)
    return do_func


@my_decorator
def my_func(list):
    pass


my_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

a = 'Hello, world!'
