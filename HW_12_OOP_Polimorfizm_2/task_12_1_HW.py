class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):  # ==

        pass

    def __ne__(self, other):  # !=

        pass

    def __ge__(self, other):  # >=

        pass

    def __le__(self, other):  # <=

        pass

    def __lt__(self, other):  # <

        pass

    def __gt__(self, other):  # >

        pass

    def __add__(self, other):  # +

        pass

    def __sub__(self, other):  # -

        pass

    def __mul__(self, other):  # *

        pass

    def __print__(self):

        pass

    def my_func(self):

        minutes = self.seconds // 60

        self.seconds = self.seconds % 60

        hours = (self.minutes + minutes) // 60

        self.minutes = (self.minutes + minutes) % 60

        days = (self.hours + hours) // 24

        self.hours = (self.hours + hours) % 24

        print('[', days, ':', self.hours, ':', self.minutes, ':', self.seconds, ']')


a = MyTime(27, 73, 88)


a.my_func()

