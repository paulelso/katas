def  main():
    s =  input("Enter an list of numbers: ").strip()
    old = [int(item) for item in s.split(',')]
    n = int(input("Enter a number: "))
    print(delete_nth(old, n))
    

def delete_nth(order,max_e):
    return [num for i, num in enumerate(order) if order[:i].count(num) < max_e]


if __name__ == "__main__":
    main()


