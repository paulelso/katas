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
        

if __name__ == '__main__':
    print(my_sum(1, 2, 3, 4, 5))
    print(my_sum([1, 2, 3], 4))
    print(my_sum(1, 2, 3, 4, 5, 'a', 'b', 'c', sep=';'))
    print(my_sum(1, 2, 3, 4, 5, 'a', 'b', 'c'))
    print(my_sum(1, 2, 3, 4, 5, 'a', 'b', 'c', sep=';'))
    print(my_sum(1, 2, 3, 4, 5, 'a', 'b', 'c', 'd'))
