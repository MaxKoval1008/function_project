from datetime import datetime
from time import sleep


class MyTime:

    def __init__(self, name, task_name, minutes, seconds, b_minutes, b_seconds):
        self.name = name
        self.task_name = task_name
        self.minutes = minutes
        self.seconds = seconds
        self.b_minutes = b_minutes
        self.b_seconds = b_seconds
        with open('HW_14_2.txt', 'a') as my_file:
            my_file.writelines(self.name)
            my_file.writelines('\n')
            my_file.writelines(self.task_name)
            my_file.writelines('\n')
            my_file.writelines(str(datetime.now()))
            my_file.writelines('\n')

    def my_func(self):

        minutes = self.seconds // 60

        self.seconds = self.seconds % 60

        self.minutes = (self.minutes + minutes) % 60

        time = [self.minutes, self.seconds]

        b_minutes = self.b_seconds // 60

        self.b_seconds = self.b_seconds % 60

        self.b_minutes = (self.b_minutes + b_minutes) % 60

        b_time = [self.b_minutes, self.b_seconds]

        print(time)

        n = 0
        while n < 4:
            if time[1] > 0:
                time[1] -= 1
                sleep(1)
                print(time)
            elif time[0] > 0:
                time[0] -= 1
                time[1] = 59
                sleep(1)
                print(time)
            else:
                with open('HW_14_2.txt', 'a') as my_file:
                    my_file.writelines('Break cycle:')
                    my_file.writelines('\n')
                    my_file.writelines(str(datetime.now()))
                    my_file.writelines('\n')

                print('Time to break!!!')

                print(b_time)

                while True:
                    if b_time[1] > 0:
                        b_time[1] -= 1
                        sleep(1)
                        print(b_time)
                    elif b_time[0] > 0:
                        b_time[0] -= 1
                        b_time[1] = 59
                        sleep(1)
                        print(b_time)
                    else:
                        with open('HW_14_2.txt', 'a') as my_file:
                            my_file.writelines('Work cycle:')
                            my_file.writelines('\n')
                            my_file.writelines(str(datetime.now()))
                            my_file.writelines('\n')
                        print('Time to work!!!')
                        n += 1
                        time = [m, s]
                        print(time)
                        b_time = [b_m, b_s]
                        break


n = input('Enter ur Name: ')
t_n = input('Enter the task name: ')
try:
    m = int(input('Enter work minutes: '))
    s = int(input('Enter work seconds: '))
except ValueError:
    m = 25
    s = 0

try:
    b_m = int(input('Enter break minutes: '))
    b_s = int(input('Enter break seconds: '))
except ValueError:
    b_m = 5
    b_s = 0

timer = MyTime(n, t_n, m, s, b_m, b_s)

timer.my_func()
