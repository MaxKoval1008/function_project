my_file = open('test.txt')
while True:
    line = my_file.readline()
    if not line:
        break
    print(line)
my_file.close()
