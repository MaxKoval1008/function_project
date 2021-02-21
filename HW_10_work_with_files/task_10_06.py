with open('task_10_06_1.txt') as my_file_1:
    text_1 = my_file_1.readlines()
with open('task_10_06_2.txt') as my_file_2:
    text_2 = my_file_2.readlines()

n = 0
while text_1[n] == text_2[n]:
    n += 1
    continue
else:
    n += 1
    print('Number of different string = ', n)
