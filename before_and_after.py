# Description: A function that takes a float and two integers (before and after). 
# Prints a float consisting of before digits before the decimal point and after digits after. 
# Thus, if the user enters 1234.5678 3 2 the program should print 234.56. 
def main():
    input_str = input("Enter a float number and two integers (before and after): ")
    before_and_after(input_str)


def before_and_after(s):
    try:
        float_num, before, after = s.split(" ")
    except ValueError:
        print("Invalid input.")
        main()
    decimal = float_num.find(".")
    if decimal == -1:
        print("Invalid input.")
        main()
    if not float_num.replace(".","").isdigit():
        print("Invalid input.")
        main()
    float_num = float_num[decimal-int(before):decimal+int(after)+1]
    print(f"{float(float_num)}")


if __name__ == "__main__":
    main()