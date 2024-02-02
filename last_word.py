# Description: Find last word, alphabetically, in a file
def find_last_word():
    with open("./file.txt", "w") as file:
        file.write("apple banana cherry date elderberry fig grapefruit honeydew kiwi lemon mango nectarine orange pear quince raspberry strawberry zucchini tangerine ugli fruit valencia orange watermelon xigua yellow passion fruit\n")

    with open("./file.txt", "r") as file:
        words = file.read().split()
        first_word = min(words, key=str.lower) 
        last_word = max(words, key=str.lower) # key is a function that is used to compare values
        print("The first word alphabetically is:", first_word)
        print("The last word alphabetically is:", last_word)        


if __name__ == "__main__":
    find_last_word()      
