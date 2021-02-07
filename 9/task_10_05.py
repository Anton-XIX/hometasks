# Имеется текстовый файл. Все четные строки этого файла
# записать во второй файл, а нечетные — в третий файл.
# Порядок следования строк сохраняется.

data_1 = []
data_2 = []

with open('test.txt') as my_file:
    data = my_file.readlines()
    for x in range(0,len(data)):
        if x % 2 != 0:
            data_1.append(data[x])
        elif x % 2 == 0:
            data_2.append(data[x])


with open('even.txt','w') as my_file:
    for x in data_1:
        my_file.write(x)


with open('not_even.txt','w') as my_file:
    for x in data_2:
        my_file.write(x)