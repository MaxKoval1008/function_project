from datetime import datetime


def my_decorator(func):
    def show_time():
        time = datetime.now()
        return time

    return show_time


@my_decorator
def my_func():
    pass


my_new_func = my_decorator(my_func)
print(my_new_func())
