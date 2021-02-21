with open('../HW_9_Decorator/test_1.txt', 'w') as my_file:
    n = 0
    while True:
        text = input('Enter smth ')
        my_file.writelines([f'{text}\n'])
        n += 1
        if n == 5:
            break