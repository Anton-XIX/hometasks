double_key_dict = lambda **kwargs: {keys+keys:values for keys, values in kwargs.items()}
print(double_key_dict(a=4, number=11, car='BMW', value=774))