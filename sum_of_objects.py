# Function that takes a list of objects and returns 
# the sum of all the objects that are either integers 
# or can be turned into integers, ignoring the other objects.
def get_sum(l):
    sum_of_ints = 0
    for i in l:
        if isinstance(i, int):
            sum_of_ints += i
        elif isinstance(i, str):
            if i.isdigit():
                sum_of_ints += int(i)
    return sum_of_ints

    
if __name__ == '__main__':
    my_list = [1, 'a', 'b', '4', 5, 6, 1.1, '1.2']
    print(get_sum(my_list))