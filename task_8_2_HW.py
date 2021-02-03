old_dict = {'aa': 1, 'b': 2,'cccc' : 3}
new_dict = {key + key: value for key, value in old_dict.items()}

print(new_dict)


old_dict2 = {'aa': 1, 'b': 2, 'cccc': 3}

for key, values in old_dict2:
    key = lambda key: key + key, old_dict2.items()
    new_keys = values

print(new_dict)
