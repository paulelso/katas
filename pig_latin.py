# Description: Pig Latin is a game of alterations played on the English language game.
# If word begins with a vowel, add 'way' to end
# If word does not begin with a vowel, put first letter at the end, then add 'ay'
def pig_latin():
    word = input("Enter a word: ")
    if (word[0]).lower in 'aeiou':
        if (word[0]).isupper():
            word = f'{word[1:].capitalize}{word[0]}way'
        else:
            word = f'{word[1:]}{word[0]}way'
        return 
    
    return f'{word[1:]}{word[0]}ay' # first letter is not a vowel
    

if __name__ == "__main__":
    print(pig_latin())