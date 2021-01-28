def get_even_keys(**kwargs):
    for key in kwargs.keys():
        if len(key) % 2 == 0:
            print(f'{key}')
    return 0


get_even_keys(a=5, true=1, false=0, fruit='apple', nine=9)
