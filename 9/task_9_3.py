#Создать декоратор для функции, которая принимает список чисел.
#Декоратор должен производить предварительную проверку данных -
#удалять все четные элементы из списка.

def delete_even_elements(func):
    def delete_elements():
        user_input = func()
        return user_input,list(filter(lambda number: number % 2 != 0, user_input))
    return delete_elements

@delete_even_elements
def input_numbers():
    user_data = []
    n = int(input('Type number of elements\n'))
    for number in range(0, n):
        user_data.append(int(input('Type number\n')))
    return user_data

print(input_numbers()[1])