a = int(input('a: '))
b = int(input('b: '))
try:
    result = a / b

except ZeroDivisionError as err:  # err - локальная переменная, as - присваивает значение в переменную err
    print(f'b is zerro - {err}!!!')
except Exception as err:
    print(f'SOMTHING WRONG - {err}!!!')
else:
    print('Result: ', result)  # выполняется в случае если ошибок не было найдено
finally:
    print('Thank you!')  # выполняется в любом случае
