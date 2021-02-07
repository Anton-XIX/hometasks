import csv


def read_file(filename):
    with open(filename, 'r') as csvfile:
        for row in csv.reader(csvfile):
            print('{:<10} {:<5} {:<5} {:<30}'.format(*row))


def write_data(filename):
    with open(filename, 'w') as csvfile:
        csv.writer(csvfile).writerows(collect_data())


def delete_row(filename, index=0):
    with open(filename, 'r') as csvfile:
        data = list(csv.reader(csvfile))
        if len(data) < index or len(data) == 0:
            print('There is no such string number')
            return 0
        data.pop(index - 1)

    with open(filename, 'w') as csvfile:
        csv.writer(csvfile).writerows(data)


def add_row(filename, index=-1):
    with open(filename, 'r') as csvfile:
        input_row = input('Input data(use , as delimiter\n').split(',')
        data = list(csv.reader(csvfile))
        if index == -1:
            data.append(input_row)
        else:
            data.insert(index - 1, input_row)

        with open(filename, 'w') as csvfile:
            csv.writer(csvfile).writerows(data)


def collect_data():
    print('Type product information(use , to separate columns)\nType 0 to stop input')
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


def calculate_sum(filename):
    with open(filename, 'r') as csvfile:
        summ = 0
        for row in csv.reader(csvfile):
            summ += int(row[1]) * int(row[2])
        return summ


def find_max_cost(filename):
    costs = []
    with open(filename, 'r') as csvfile:
        for row in csv.reader(csvfile):
            costs.append(int(row[1]))
    return sorted(costs)[-1]


def find_min_cost(filename):
    costs = []
    with open(filename, 'r') as csvfile:
        for row in csv.reader(csvfile):
            costs.append(int(row[1]))
    return sorted(costs)[0]


def reduce_amount(filename):
    with open(filename, 'r') as csvfile:
        data = [row for row in csv.reader(csvfile)]

    line_num = int(input('Enter line number where reduce amount \n')) - 1
    while line_num > len(data) - 1:
        line_num = int(input('Enter correct line number\n')) - 1
    reduce_num = int(input('Enter number for reducing count of product\n'))
    intermin_data = 0
    if int(data[line_num][2]) >= reduce_num:
        intermin_data = int(data[line_num][2])
        intermin_data -= reduce_num
    data[line_num][2] = intermin_data
    with open(filename, 'w') as csvfile:
        csv.writer(csvfile).writerows(data)
    return data
