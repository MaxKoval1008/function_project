old_dict = {'aa': 1, 'b': 2,'cccc' : 3}
new_dict = {key:value for value, key in old_dict.items()}

print(new_dict)