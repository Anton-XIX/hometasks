# Создать csv файл с данными о ежедневной погоде. Структура: Дата,
# Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
# градусы) для Минск за последние 7 дней.

import csv
import os.path

from datetime import datetime, timedelta


def write_data(filename):
    with open(filename, 'w') as csvfile:
        csv.writer(csvfile).writerows(collect_data())


def collect_data():
    print('Type data)\nType 0 to stop input')
    output_data = []
    while True:
        user_data = input()
        if user_data[0] == '0' and len(user_data) == 1:
            break
        else:
            if len(user_data.split(',')) < 4 or len(user_data.split(',')) > 4:
                print('Error format of input')
                continue
            else:
                output_data.append(user_data.split(','))
    return output_data


def get_last_weather(filename):
    output_data = []
    with open(filename, 'r') as csvfile:
        for row in csv.reader(csvfile):
            if datetime.strptime(row[0], '%Y.%m.%d') >= datetime.today() - timedelta(days=7) and row[1].lower() == 'minsk':
                output_data.append(row)
        if len(output_data) == 0:
            return f'No any data for 7 days'
        else:
            return output_data


if os.path.exists('weather.csv'):
    for data in get_last_weather('weather.csv'):
        print('{:<10} {:<5} {:<5} {:<30}'.format(*data))
else:
    write_data('weather.csv')
    for data in get_last_weather('weather.csv'):
        print('{:<10} {:<5} {:<5} {:<30}'.format(*data))
