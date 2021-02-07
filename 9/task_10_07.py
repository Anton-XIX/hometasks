# Создать матрицу случайных чисел и сохранить ее в json
# файл. После прочесть ее, обнулить все четные элементы
# и сохранить в другой файл

import json
from random import randint


def create_matrix(size_n, size_m):
    return [[randint(0, 8) for n in range(0, size_n)] for m in range(0, size_m)]


with open('json_10_07.txt', 'w') as my_file:
    my_file.write(json.dumps(create_matrix(2, 2)))

with open('json_10_07.txt') as my_file:
    data = json.loads(my_file.read())
    print(f'Data from file: {data}')
    for line in data:
        for element in line:
            if element % 2 == 0:
                data[data.index(line)][line.index(element)] = 0

with open('result_json_10_07.txt', 'w') as my_file:
    my_file.write(json.dumps(data))
    print(f'New data from file: {data}')
