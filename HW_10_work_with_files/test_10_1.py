import json
with open('test_10_1.txt', 'w') as my_file:
    data = json.dumps({'a': 5})
    my_file.write(data)

with open('test_10_1.txt') as my_file:
    data = json.loads(my_file.read())
    print(data)
