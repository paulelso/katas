import random

def get_user_selection():
    user_selection = input("Selec R for Rock, P for Paper, or S for Scissors: ")
    user_selection = user_selection.lower()
    if user_selection not in ['r', 'p', 's']:
        print("Invalid selection")
        return get_user_selection()
    return user_selection


def get_computer_selection():
    computer_selection = random.choice(['r', 'p', 's'])
    return computer_selection


def get_winner(user_selection, computer_selection):
    if user_selection == computer_selection:
        return "It's a tie"
    elif user_selection == 'r' and computer_selection == 's':
        return "Rock beats Scissors. You win!"
    elif user_selection == 'p' and computer_selection == 'r':
        return "Paper beats Rock. You win!"
    elif user_selection == 's' and computer_selection == 'p':
        return "Scissors beats Paper. You win!"
    elif computer_selection == 'r' and user_selection == 's':
        return "Rock beats Scissors. You lose!"
    elif computer_selection == 'p' and user_selection == 'r':
        return "Paper beats Rock. You lose!"
    elif computer_selection == 's' and user_selection == 'p':
        return "Scissors beats Paper. You lose!"
    

if __name__ == "__main__":
    user_selection = get_user_selection()
    computer_selection = get_computer_selection()
    print(get_winner(user_selection, computer_selection))