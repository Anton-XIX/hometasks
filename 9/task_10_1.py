# Создать csv файл с данными следующей структуры: Имя, Фамилия,
# Возраст. Создать отчетный файл с информацией по количеству людей
# входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
# 19-25, 26-40, 40+.

import csv
import os.path


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
            if len(user_data.split(',')) < 3 or len(user_data.split(',')) > 3:
                print('Error format of input')
                continue
            else:
                output_data.append(user_data.split(','))
    return output_data


def get_age(filename):
    output_data = {'1-12': 0,
                   '13-18': 0,
                   '19-25': 0,
                   '26-40': 0,
                   '40+': 0
                   }

    with open(filename, 'r') as csvfile:
        for row in csv.reader(csvfile):
            for key in output_data.keys():
                if key == '40+' or int(row[2]) <= int(key[-2:]):
                    output_data[key] += 1
                    break
            print('{:<10} {:<8} {:<8}'.format(*row))

    with open('result.csv', 'w') as csvfile:
        csv.writer(csvfile).writerows([[key, value] for key, value in output_data.items()])
    return 0


if os.path.exists('ages.csv'):
    get_age('ages.csv')
else:
    write_data('ages.csv')
    get_age('ages.csv')
