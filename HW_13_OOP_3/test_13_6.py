a = int(input('a: '))
b = int(input('b: '))

if b == 0:
    raise ZeroDivisionError('b is zero')  # вызывает ошибку в коде красным с прерыванием действия
summ = a + b

print(summ)
