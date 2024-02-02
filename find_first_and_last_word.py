# Description: Function that reads a file and prints the first and last word.
def find_first_and_last_word(file):
    words = file.read().split()
    first_word = min(words, key=str.lower)
    last_word = max(words, key=str.lower)
    print(f"The first word alphabetically is: {first_word}.")
    print(f"The last word alphabetically is: {last_word}.")


if __name__ == "__main__":
    with open("./file.txt", "w") as file:
        file.write("apple banana cherry date elderberry fig grapefruit honeydew kiwi lemon mango nectarine orange pear quince raspberry strawberry zucchini tangerine ugli fruit valencia orange watermelon xigua yellow passion fruit\n")

    with open("./file.txt", "r") as file:
        find_first_and_last_word(file)    
