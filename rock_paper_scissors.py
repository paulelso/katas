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


def get_winner(p1, p2):
    options = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    p1 = options[p1]
    p2 = options[p2]
    combinations = [('r', 's'), ('s', 'p'), ('p', 'r')]
    scores = f"You: {p1} vs Computer: {p2}."
    if (p1, p2)  in combinations:
        winner = f"{scores} You win!"
    elif (p2, p1) in combinations:
        winner = f"{scores} Computer wins!"
    else:
        winner = f"{scores} It's a tie"

    return winner


if __name__ == "__main__":
    user_selection = get_user_selection()
    computer_selection = get_computer_selection()
    print(get_winner(user_selection, computer_selection))