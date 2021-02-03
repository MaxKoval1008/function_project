def my_decorator(func):
    def do_some_staff():
        print('Hello, world!')
        result = func()
        # some action
        return result

    return do_some_staff


@my_decorator  # отдельно выполняет функцию
def my_func():
    pass


my_new_func = my_decorator(my_func)
my_new_func()
