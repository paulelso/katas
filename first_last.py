# Description: Function that takes a string and returns the first and last word in the string.
def first_last(s):
    string_list = s.split(' ')
    return f'{string_list[0]}, {string_list[-1]}'


if __name__ == "__main__":
    print(first_last('python'))
    print(first_last('python is awesome'))
    print(first_last('python is awesome and easy'))
    print(first_last('python is awesome and easy to learn'))
    print(first_last('python is awesome and easy to learn and it is fun'))
    print(first_last('python is awesome and easy to learn and it is fun and it is great'))
    print(first_last('python is awesome and easy to learn and it is fun and it is great and it is amazing'))