with open('../HW_9_Decorator/test_2.txt') as my_file:
    text_old = my_file.readlines()

with open('../HW_9_Decorator/test_3.txt', 'w') as new_file:
    for i in text_old:
        for j in i:
            if j == '0':
                j = '1'
            elif j == '1':
                j = '0'
            new_file.write(j)
        #new_file.write(i)
