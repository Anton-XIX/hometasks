import time
from time import gmtime


class MyTime:
    def __init__(self, *args):
        time_struct = time.localtime()

        if len(args) == 3:
            time_struct = gmtime(args[0] * 3600 + args[1] * 60 + args[2])
        elif len(args) == 1:
            if isinstance(args[0], str):
                arg = args[0].split(':')
                time_struct = gmtime(int(arg[0]) * 3600 + int(arg[1]) * 60 + int(arg[2]))
            else:
                time_struct = gmtime(args[0].hours * 3600 + args[0].minutes * 60 + args[0].seconds)

        self.__hours = time_struct.tm_hour
        self.__minutes = time_struct.tm_min
        self.__seconds = time_struct.tm_sec

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours):
        self.__hours = hours

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes):
        self.__minutes = minutes

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds):
        self.__seconds = seconds

    def __eq__(self, other):
        return self is other

    def __ne__(self, other):
        return self is not other

    def __le__(self, other):
        time_1 = gmtime((self.__hours) * 3600 + (self.__minutes) * 60 + (self.seconds))
        time_2 = t = gmtime((other.__hours) * 3600 + (other.seconds) * 60 + (other.seconds))
        return time_1 <= time_2

    def __ge__(self, other):
        time_1 = gmtime((self.__hours) * 3600 + (self.__minutes) * 60 + (self.seconds))
        time_2 = t = gmtime((other.__hours) * 3600 + (other.seconds) * 60 + (other.seconds))
        return time_1 >= time_2

    def __gt__(self, other):
        time_1 = gmtime((self.__hours) * 3600 + (self.__minutes) * 60 + (self.seconds))
        time_2 = t = gmtime((other.__hours) * 3600 + (other.seconds) * 60 + (other.seconds))
        return time_1 > time_2

    def __lt__(self, other):
        time_1 = gmtime((self.__hours) * 3600 + (self.__minutes) * 60 + (self.seconds))
        time_2 = t = gmtime((other.__hours) * 3600 + (other.seconds) * 60 + (other.seconds))
        return time_1 < time_2

    def __add__(self, other):
        t = gmtime((self.__hours + other.__hours) * 3600 + (self.__minutes + other.seconds) * 60 + (
                    self.seconds + other.seconds))
        return f'{t.tm_hour}:{t.tm_min}:{t.tm_sec}'

    def __sub__(self, other):
        t = gmtime((self.__hours - other.__hours) * 3600 - (self.__minutes - other.seconds) * 60 + (
                self.seconds - other.seconds))
        return f'{t.tm_hour}:{t.tm_min}:{t.tm_sec}'

    def __mul__(self, other):
        if type(other) == int:
            t = gmtime((self.__hours * other) * 3600 - (self.__minutes * other) * 60 + (self.seconds * other))
            return f'{t.tm_hour}:{t.tm_min}:{t.tm_sec}'
        else:
            return 'Incorrect input'

    def get_time(self):
        return f'{self.__hours}:{self.__minutes}:{self.__seconds}'

