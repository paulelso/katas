def main():
    s = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"),
        ("rock", "rock"), ("scissors", "scissors"), ("paper", "paper")]
    for _ in s:
        print(rps(_[0], _[1]))


def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock") or (p1 == "rock" and p2 == "scissors"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"
                
        
if __name__ == "__main__":
    main()