# Description: A function that takes two strings as input 
# and returns True if they are anagrams, and False otherwise.
def is_anagram(input1, input2):
    input1 = sorted(input1.lower().strip())
    input2 = sorted(input2.lower().strip())
    return input1 == input2


if __name__ == "__main__":
    print(is_anagram('iceman', 'cinema'))
    print(is_anagram('leaf', 'tree'))
    print(is_anagram('save', 'vase'))
    print(is_anagram('dusty', 'study '))
    print(is_anagram('angel', 'glean'))
    print(is_anagram('state', 'taste'))
    print(is_anagram('angel', 'angle'))
    print(is_anagram('dusty', 'study '))