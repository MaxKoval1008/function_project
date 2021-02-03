old_dict = {'aa': 1, 'b': 2,'cccc' : 3}
new_dict = {key + key: value for key, value in old_dict.items()}

print(new_dict)


double_key = lambda **kwargs: {key + key: value for key, value in kwargs.items()}

print(double_key(aa=1, b=2, cc123cc=3))
