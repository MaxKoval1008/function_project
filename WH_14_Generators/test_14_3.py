def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i * i  # используется вместо return для возврата значения из генератора


mygenerator = create_generator()
print(mygenerator)  # <generator object create_generator at 0x7f9569fbe9e0> - результат вывода, обращение к генератору происходит через цикл for

for i in mygenerator:  # использование генератора
    print(i)
