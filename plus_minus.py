# Description: Function that takes a list or tuple of numbers and returns 
# the result of alternately adding and subtracting numbers from each other.
def plus_minus(lst):
    result = 0
    for i, num in enumerate(lst):
        if i == 0:
            result = num
        elif i % 2 != 0:
            result += num
        else:
            result -= num

    return result    
    

if __name__ == "__main__":
    print(plus_minus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))# 7 
    print(plus_minus([10, 20, 30, 40, 50, 60]))# 50
