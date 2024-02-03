# Description: Function that takes a list or tuple of numbers. Return a two-element list,
# containing (respectively) the sum of the even-indexed numbers and the sum of
# the odd-indexed numbers.
def sum_of_indexes(lst):
    sum_of_odd_indexes = 0
    sum_of_even_indexes = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            sum_of_even_indexes += lst[i]
        else:
            sum_of_odd_indexes += lst[i]
 
    return ([sum_of_even_indexes, sum_of_odd_indexes]) 

if __name__ == "__main__":
    print(sum_of_indexes([1, 2, 3, 4, 5, 6, 7, 8, 9])) # 25 20
    print(sum_of_indexes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 55 30
    print(sum_of_indexes([10, 20, 30, 40, 50, 60])) # 90 120
