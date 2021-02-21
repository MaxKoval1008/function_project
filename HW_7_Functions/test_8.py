# def func(*arg):
#     n = 0
#     summ = 0
#     max_num1 = 0
#     max_num2 = 1
#     max_sence = 0
#     for i in arg:
#         summ += arg[n]
#         n += 1
#     for j in arg:
#         if arg[max_num1] < arg[max_num2] and max_num2 + 1 < len(arg) - 1:
#             max_num1 += 1
#         else:
#             max_sence = arg[max_n]
#     print(summ, max_sence)
#     return arg
#
# func(111, 2, 4, 88, 6, 7, 10, 0, 24, 900)


def sorting(*args):
    summ = 0
    n = 0
    maxim = 0
    for i in args:
        summ += i
        if i > args[-1] and i > maxim:
            maxim = i
        n += 1
    return summ, maxim


summ, maxim = sorting(1, 45, 6, 2, 5, 3)
print(maxim)