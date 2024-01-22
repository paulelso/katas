# Description: A function that asks the user for their name and 
# then prints a "triangle name": first letter of  their name +
# first two letters of their name + first three letters of their name, etc.
def triangle_name():
    name = input("Enter your name: ")
    count = 1
    triangle_name = ""
    for i in name:
        triangle_name += name[0:count]
        count += 1
    return triangle_name


if __name__ == '__main__':
    print(triangle_name())

