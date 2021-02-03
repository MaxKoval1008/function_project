# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.

name2 = ['aaa', 'bbbb', 'cccc', 'ddddd']

hello_name = [f'{str(name2.index(i))} - {i}' for i in name2]

print(hello_name)
