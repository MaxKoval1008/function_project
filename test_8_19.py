from functools import reduce

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


sum_all = reduce(lambda x, y: x * y, filter(lambda x: x % 3 == 0, items))

print(sum_all)