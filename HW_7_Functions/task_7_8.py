def average(*args):
    n = 0
    sum_aver = 0
    for i in args:
        sum_aver += i
        continue
    aver = sum_aver / len(args)
    print(aver)
    return args


def geometric_mean(*args):
    l = 1
    for i in args:
        l *= i
        continue
    g_m = l ** (1 /8)
    print(g_m)
    return args


def task(*args, **kwargs):
    for key, values in kwargs.items():
        for n in values:
            print(n)
            if n == 'G':
                geometric_mean(args)
            elif n == 'A':
                average(args)
            else:
                print('Wrong option ')
                continue
    return args, kwargs


average(1, 10, 6, 18, 45)

geometric_mean(1, 10, 6, 18, 45)

task(1, 10, 6, 18, 45, mean_type='G')
