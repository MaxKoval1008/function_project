with open('test.txt') as my_file:   #открывает файл в переменной my_file для дальнейшего использования
    for line in my_file.readline():
        print(line)
