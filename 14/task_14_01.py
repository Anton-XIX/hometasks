import logging
import datetime
from time import sleep, strftime, localtime


class Timer:
    def __init__(self, name: str, surname: str, hours: int, minutes: int, seconds: int):
        self.__name = name
        self.__surname = surname
        self.__time_struct = datetime.datetime(1, 1, 1, hour=hours, minute=minutes, second=seconds)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        logger_handler = logging.FileHandler('task_13_1_log.log')
        logger_handler.setLevel(logging.INFO)
        logger_format = logging.Formatter('%(message)s')
        logger_handler.setFormatter(logger_format)
        self.logger.addHandler(logger_handler)

    def log_timer(self):
        self.logger.info(f'User: {self.__name} {self.__surname} - {strftime("%H:%M:%S", localtime())}')

    def start_timer(self):
        self.log_timer()
        while self.__time_struct.hour * 3600 + self.__time_struct.minute * 60 + self.__time_struct.second > 0:
            print(self.__time_struct.time())
            self.__time_struct -= datetime.timedelta(seconds=1)
            sleep(1)
        print('ALARM!!!!!')
        self.logger.info(f'ALARM AT TIME {strftime("%H:%M:%S", localtime())} for {self.__name} {self.__surname}')


a = Timer('John', 'Petrov', 0, 0, 3)
a.start_timer()
