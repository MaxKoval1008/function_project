names = ['John', 'Ivan', 'Max', 'Sam', 'Vlad']
n = 0
def pr_name(a):
    print(f'Hello, {a}')
    return a
for i in names:
    pr_name(names[n])
    n += 1
