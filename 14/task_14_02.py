import logging
import datetime
from time import sleep, strftime, localtime, gmtime


class Timer:
    def __init__(self, name, surname,task_name, focus_time, break_time=5, num_of_cycles=4):
        self.__name = name
        self.__surname = surname
        self.__task_name = task_name
        self.__focus_time = focus_time * 60
        self.__break_time = break_time * 60
        self.__num_of_cycles = num_of_cycles

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        logger_handler = logging.FileHandler('task_14_1_log.log')
        logger_handler.setLevel(logging.INFO)
        logger_format = logging.Formatter('%(message)s')
        logger_handler.setFormatter(logger_format)
        self.logger.addHandler(logger_handler)

    def log_timer(self):
        self.logger.info(f'User: {self.__name} {self.__surname}-{strftime("%H:%M:%S", localtime())},'
                         f'Focus time:{self.__focus_time} Break time:{self.__break_time}, Task: {self.__task_name}')

    def start_focus(self):
        self.log_timer()

        while self.__num_of_cycles > 0:
            work_time = self.__focus_time
            break_time = self.__break_time
            print('WORKING TIME!')
            while work_time > 0:
                print(f'Time to work: {strftime("%H:%M:%S", gmtime(work_time))}')
                work_time -= 1
                sleep(1)
            print('BREAK TIME!')
            while break_time > 0:
                print(f'Time for rest: {strftime("%H:%M:%S", gmtime(break_time))}')
                break_time -= 1
                sleep(1)
            self.__num_of_cycles -= 1
        print('HAVE A REST')


a = Timer('John', 'Petrov','Homework', 0.1, 0.1, 3)
a.start_focus()
