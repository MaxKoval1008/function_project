from datetime import datetime
from time import sleep


class MyTime:
    def __init__(self, name,  hours, minutes, seconds):
        self.name = name
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        with open('HW_14_1.txt', 'a') as my_file:
            my_file.writelines(self.name)
            my_file.writelines('\n')
            my_file.writelines(str(datetime.now()))

    def my_func(self):

        minutes = self.seconds // 60

        self.seconds = self.seconds % 60

        hours = (self.minutes + minutes) // 60

        self.minutes = (self.minutes + minutes) % 60

        self.hours = (self.hours + hours)

        time = [self.hours, self.minutes, self.seconds]

        print(time)

        while True:
            if time[2] > 0:
                time[2] -= 1
                sleep(1)
                print(time)
            elif time[1] > 0:
                time[1] -= 1
                time[2] = 59
                sleep(1)
                print(time)
            elif time[0] > 0:
                time[0] -= 1
                time[1] = 59
                time[2] = 59
                sleep(1)
                print(time)
            else:
                print('ALARM!!!')
                print(f'Wake up, {self.name}!')
                break


n = input('Enter ur Name: ')
h = int(input('Enter Hours: '))
m = int(input('Enter minutes: '))
s = int(input('Enter Seconds: '))

timer = MyTime(n, h, m, s)

timer.my_func()

