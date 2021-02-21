def my_format(string, char='!'): #задает значение по умолчанию, если второй аргумент будет отсутствовать
    result_string = f'{char}{string}{char}'
    return result_string


print(my_format('Hello'))

