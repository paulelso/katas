import random

def get_answer():
    while True:
        user_input = input('Guess a number between 1 and 100: ')
        if user_input.isdigit() and 1 <= int(user_input) <= 100:
            return int(user_input)
        else:
            print('Enter an integer between 1 and 100: ')


def guessing_game():
    answer = random.randint(1, 100) # Generate random number between 1 and 100 (inclusive)
    count = 0
    while count < 3:
        count += 1
        guess = get_answer()
        if guess < answer:
            print('Too low')
        elif guess > answer:
            print('Too high')
        else:
            print('Just right')
            break


if __name__ == '__main__':
    guessing_game()