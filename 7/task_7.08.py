def get_average(data):
    result = 0
    for item in data:
        result += item
    result /= len(data)
    return result


def get_geometric_mean(data):
    result = 1
    for item in data:
        result *= item
        result = pow(result, 1/len(data))
    return result


def call_calculation_function(*args, mean_type):
    if mean_type.lower() == 'average':
        return get_average(args)
    elif mean_type.lower() == 'geometric':
        return get_geometric_mean(args)
    else:
        print('Incorrect input')


print(call_calculation_function(1, 44, 55, 11, 45,
                                mean_type=input("Type average or geometric for calculation\n")))



