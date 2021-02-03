with open('test_1.txt', 'a') as my_file:
    n = 0
    while True:
        text = input('Enter smth ')
        my_file.writelines([f'{text}\n'])
        n += 1
        if n == 3:
            break
