mylist = [1, 2, 3]
for i in mylist:
    print(i)

mylist2 = [x*x for x in range(3)]  # генератор
for i in mylist2:
    print(i)
