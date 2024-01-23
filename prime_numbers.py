import math
# Description: A Python function that takes an integer as input 
# and returns True if it's a prime number, and False otherwise.
def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    # iterate over the range of numbers from 2 to the square root of n 
    # and check if n is divisible by any of those numbers.
    # If it is, the code returns False, indicating that n is not a prime number.
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    numbers = ["36", "97", "53", "7", "8", "9"]
    for number in numbers:
        print(is_prime(number))

