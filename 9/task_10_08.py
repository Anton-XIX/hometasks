# Написать функции по работе с csv файлами в файле csv_utils.py. Чтение.
# Запись. Добавление записи(по позиции, по-умолчанию в конец). Удаление
# записи(по позиции, по-умолчанию последнюю).
# В файле task_10_08 импортировать функции. С помощью функций создать
# файл с информацией о товарах(Имя товара, цена, количество,
# комментарий).
# Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.

from csv_utils import *

# write_data('new_file.csv') #Поля разделяются запятой, строки клавишой enter. Уберите #, если хотите создать файл с нуля
read_file('new_file.csv')
add_row('new_file.csv')
delete_row('new_file.csv', 3)
print(calculate_sum('new_file.csv'))