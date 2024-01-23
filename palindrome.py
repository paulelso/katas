# Description: Python function to check if a given string is a palindrome.
# The function should return True if the string is a palindrome and False otherwise.
def is_palindrome(word):
    return word == word[::-1] # compares original string to original string in reverse order.


if __name__ == "__main__":
    palindromes = ["civic", "radar", "noon", "madam", "level", "racecar", "none", "zoom", "carrot", "hello"]
    for palindrome in palindromes:
        print(is_palindrome(palindrome))