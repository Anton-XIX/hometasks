# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный.


def change_args_order(func):
    def change_order(*args):
        return func(*args[::-1])
    return change_order


@change_args_order
def fun(surname, id, number):
    return surname, id, number


print(fun('1st arg', 2, 'Third arg'))