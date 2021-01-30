def my_func(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

    return kwargs


my_func(a=5)
