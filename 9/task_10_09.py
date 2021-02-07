# Использовать результаты 10.8. Все функции описываются в csv_utils.py.
# Проверка работы функции осуществляется в task_10_09.py.

import os.path
from csv_utils import*

if os.path.exists('new_file.csv'):
    print(calculate_sum('new_file.csv'))
    print(find_max_cost('new_file.csv'))
    print(find_min_cost('new_file.csv'))
    print(reduce_amount('new_file.csv'))
else:
    write_data('new_file.csv')
    print(calculate_sum('new_file.csv'))
    print(find_max_cost('new_file.csv'))
    print(find_min_cost('new_file.csv'))
    print(reduce_amount('new_file.csv'))