my_file = open('../HW_9_Decorator/test.txt')
line = my_file.readline()
print(line)
my_file.close()

my_file = open('../HW_9_Decorator/test.txt')
n = 0
while True:
    if n < 4:
        line = my_file.readline()
        n += 1
        continue
    else:
        line = my_file.readline()
        print(line)
        break
my_file.close()

my_file = open('../HW_9_Decorator/test.txt')
m = 1
while True:
    if m < 6:
        line = my_file.readline()
        m += 1
        print(line)
    else:
        break
my_file.close()

my_file = open('../HW_9_Decorator/test.txt')
k = 1
while True:
    if k < 3:
        line = my_file.readline()
        k += 1
        print(line)
    else:
        break
my_file.close()

my_file = open('../HW_9_Decorator/test.txt')
while True:
    line = my_file.readline()
    if not line:
        break
    print(line)
my_file.close()
