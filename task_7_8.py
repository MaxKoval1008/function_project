def average(*args):
    global aver
    n = 0
    for i in args:
        i += args[n]
        n += 1
        aver = i/len(args)
    print(aver)


def geometric_mean(*args):
    global g_m
    n = 0
    a = len(args)
    b = '0.'
    c = b + str(a)
    d = float(c)
    for i in args:
        i *= args[n]
        n += 1
        g_m = i ** c
    print(g_m)

def task(*args, mean_type):
    if mean_type.lower() == 'Average':
        average(args)
    elif mean_type.lower() == 'Geometric mean':
        geometric_mean(args)
    else:
        print('Wrong option ')
