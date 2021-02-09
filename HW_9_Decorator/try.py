# def decorator(func):
#     def inner():
#         print('Start decorator\n')
#         func()
#         print('End decorator\n')
#     return inner
#
#
# def say():
#     print('Hello, world!\n')
#
# d = decorator(say)
#
#
# d()

def bread(func):
    def wrapper():
        print()
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper

def sandwich(food="--ветчина--"):
    print(food)

sandwich()
sandwich = bread(ingredients(sandwich))
sandwich()