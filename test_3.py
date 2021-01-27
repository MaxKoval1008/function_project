def factorial(n):
    num = 0
    f = 1
    while num < n:
        num += 1
        f *= num
    print('Factorial:', f)
    return f


factorial(5)


def fact(n):
    ind = 0
    res = 1
    while ind < n:
        ind += 1
        res *= ind
    print(res)
    return res


fact(5)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))