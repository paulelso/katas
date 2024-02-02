# Description: Function that returns the longest word in the list
def find_longest_word(file):
    words = file.read().split()
    return max(words, key=len) # return the longest word in the list


if __name__ == "__main__":
    with open("./file.txt", "w") as file:
        file.write("apple banana cherry date elderberry fig grapefruit honeydew kiwi lemon mango nectarine orange pear quince raspberry strawberry zucchini tangerine ugli fruit valencia orange watermelon xigua yellow passion fruit\n")

    with open("./file.txt", "r") as file:
        print(find_longest_word(file))
