def hex_output():
    s = input("Enter a hex number to convert: ")
    conversion = 0
    for i in s:
        if ord(i) in range(48, 58):
            conversion += int(i)
        conversion *= 16
        return conversion


if __name__ == '__main__':
    print(hex_output())