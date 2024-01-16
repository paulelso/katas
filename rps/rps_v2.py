def main():
    s = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"),
         ("rock", "rock"), ("scissors", "scissors"), ("paper", "paper")]
    for _ in s:
        print(rps(_[0], _[1]))


def rps(p1, p2):
    # dictionary of winning combinations
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'} 
    if beats[p1] == p2: # if p1 beats p2
        return "Player 1 won!"
    if beats[p2] == p1: # if p2 beats p1
         return "Player 2 won!"
    return "Draw!" # otherwise a draw
                
        
if __name__ == "__main__":
    main()