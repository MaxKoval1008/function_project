def my_decorator(func):
    def do_func(my_func):
        # my_func = [i for i in my_func if i % 2 != 0] - перезаписывает переменную, а не удаляет
        # my_func = [my_func.remove(i) for i in my_func if i % 2 == 0] - почему-то не работает
        for i in my_func:
            if i % 2 == 0:
                my_func.remove(i)
        print(my_func)
    return do_func


@my_decorator
def my_func(list):
    pass


my_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
