list_a = ['Max', 'Alex', 'Anton', 'Ivan']

func = lambda name: print(f'Hello, {name}')


for i in list_a:
    func(i)

# list = [lambda x:x*i for i in range(5)]

name2 = ['qwer', 'lea', 'amir']

hello_name = lambda name: [f'Hello {i}' for i in name]

print(hello_name(name2))