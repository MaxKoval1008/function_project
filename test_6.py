def func(*arg):
    n = 0
    summ = 0
    for i in arg:
        summ += i * arg[n]
        n += 1

    print(summ)
    return arg

func(5, 4, 3, 2, 1)

