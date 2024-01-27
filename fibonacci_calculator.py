# Decription: function to generate the first n numbers in the Fibonacci sequence. 
# The function should returns a list of the Fibonacci numbers.
def generate_fibonacci_sequence(start, end):
    if start == 0:
        fibonacci_list = [0, 1]
        for i in range(2, end+1):
            fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
    elif start == 1:
        fibonacci_list = [1, 1]
        for i in range(2, end):
            fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
    else:
        fibonacci_list = [start, start+1]
        count = start+1
        while count <= end:
            fibonacci_list.append(fibonacci_list[count-2] + fibonacci_list[count-3])
            print(count, fibonacci_list[count-3]) 
            count += 1
                   
    #print(fibonacci_list)

    #return fibonacci_list[::]  # Return the list of Fibonacci numbers


def test(n):
    numbers = []
    for i in range(n):
        if i < 2:
            numbers.append(1)
        else:
            numbers.append(numbers[i-1] + numbers[i-2])
    return numbers[-1]


def fibonacci_sequence(n):
    count_list = [1, 2]
    sequence_list = [1, 1]
    count = 2
    while len(sequence_list) < n:
        count += 1
        count_list.append(count)
        next_number = sequence_list[-1] + sequence_list[-2]
        sequence_list.append(next_number)
    
    # Python’s zip() function takes in iterables as arguments and returns an iterator. 
    # This iterator generates a series of tuples containing elements from each iterable. 
    # zip() can accept any type of iterable, such as files, lists, tuples, dictionaries, sets, etc.    
    return list(zip(count_list, sequence_list))


if __name__ == "__main__":
    user_input = input("Enter Fn for n: ")
    start = int(user_input.split()[0])
    end = int(user_input.split()[1])
    generate_fibonacci_sequence(start, end)