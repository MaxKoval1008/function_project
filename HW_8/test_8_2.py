from random import randint

n_1 = 10

matrix = [randint(1, 9) for j in range(n_1)]

print(matrix)


def count(matrix):
    new_dict = {key: matrix.count(key) for key in matrix}
    return new_dict

print(count(matrix))

n = 0
diction_right_keys = {i: 1 for i in matrix}

for k, v in diction_right_keys.items():
    n = 0
    for i in matrix:
        if k == i:
            n += 1
    diction_right_keys[k] = n

print(diction_right_keys)