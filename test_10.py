def full_func(*args, **kwargs):
    print(args)
    print(kwargs.items())

    return args, kwargs


full_func(1, 2, 3, a=4, b=5, c=6)
