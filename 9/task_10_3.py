# Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
# год. Найти самую раннюю дату. [02-8.1-ML-29]

import csv
from datetime import datetime


def get_earliest_date(filename):
    with open(filename, 'r') as csvfile:
        dates = [datetime.strptime(row[0],'%Y.%m.%d') for row in csv.reader(csvfile)]
        return min(dates).date()


print(get_earliest_date('date_10_3.csv'))