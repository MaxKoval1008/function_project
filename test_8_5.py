cars = [{'model':'audi', 'year' : 1990, 's_num':'A1'},
    {'model':'bmw', 'year':2001, 's_num':'B48'},
    {'model':'mercedes', 'year':1989, 's_num':'M33'}]

n = 1990

list_a = [i for i in cars for key, value('year') in i.items() if int(value) > n]

print(list_a)

list_dicts = [{'n': 1, 'y': 1993}, {'n': 2, 'y': 1995}, {'n': 3, 'y': 1998}, {'n': 4, 'y': 1959}, {'n': 5, 'y': 1994}]
n = 1991
list_b = [i for i in list_dicts for k, v in i.items() if v > n]
print(list_b)
