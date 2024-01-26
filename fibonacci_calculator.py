def fibonacci(n):
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
    user_input = int(input("Enter Fn for n: "))
    print(fibonacci(user_input))
    print(fibonacci_sequence(user_input))