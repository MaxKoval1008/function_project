with open('task_10_05.txt') as my_file:
    text_old = my_file.readlines()


with open('task_10_05_1.txt', 'w') as new_file_1:
    for i in text_old:
        if text_old.index(i) % 2 == 0:
            new_file_1.writelines(i)
        else:
            new_file_1.writelines('\n')


with open('task_10_05_2.txt', 'w') as new_file_2:
    for i in text_old:
        if text_old.index(i) % 2 != 0:
            new_file_2.writelines(i)
        else:
            new_file_2.writelines('\n')
