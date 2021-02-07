# Имеются два текстовых файла с одинаковым числом
# строк. Выяснить, совпадают ли их строки. Если нет, то
# получить номер первой строки, в которой эти файлы
# отличаются друг от друга.

with open('test.txt') as my_file:
    file_data = my_file.readlines()
    file_data.reverse()


with open('test_2.txt') as my_file:
    file_data_2 = my_file.readlines()
    for i in file_data_2:
        if i != file_data.pop():
            print(f'Index of string is {file_data_2.index(i)+1}')
            break
    if file_data == []:
        print('Files are similar')