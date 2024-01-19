def my_sum(*args, sep=' '):
    try:
        if isinstance(args[1], int):
            sum = int(args[1])
    except:
        sum = 0
    for arg in args:
        if isinstance(arg, int):
            sum += int(arg)
    return sum


def my_average(*args, sep=' '):
    sum = 0
    for arg in args:
        if isinstance(arg, int):
            sum += my_sum(arg)
    return sum / len(args)


if __name__ == '__main__':
    print(my_average(1, 2, 3, 4, 5, 6))
    print(my_average(1, 2, 3, 4, 5, 6, sep=','))
    print(my_average(1, 2, 3, 4, 5, 6))