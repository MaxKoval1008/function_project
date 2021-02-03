def my_decorator(func):
    def do_func():
        list = func()
        new_list = [i for i in list if i % 2 == 0]
        print(new_list)
        return func(), new_list

    return do_func


@my_decorator
def my_func():
    list = [i for i in range(1, 11, 1)]
    return list


print(my_func())
