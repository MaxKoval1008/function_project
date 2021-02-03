string_names = ['Max', 'Nikolay', 'Konstantin', 'Anton', 'Ekaterina']

result = list(filter(lambda x: 'k' in x.lower(), string_names))

print(result)
