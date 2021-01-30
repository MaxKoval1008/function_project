def even_keys(**kwargs):
    for key, values in kwargs.items():
        if len(key) % 2 == 0:
            print(key, values)
    return kwargs


even_keys(firstnam='Masha', Group=1, physic=4, history=10)
