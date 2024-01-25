# Description: Function that takes a list as input and returns a new list
# containing only the unique elements, preserving the original order.
def get_unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list


if __name__ == "__main__":
    input_list = [1, 2, 3, 3, 4, 1, 2, 5, 6, 7, 8, 9, 9, "a", "e", "i", "o", "u", "a", "e", "e", "i", "o", "u" ]
    print(get_unique_elements(input_list))