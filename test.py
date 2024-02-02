with open("./file.txt", "w") as file:
    file.write("apple banana cherry date elderberry fig grapefruit honeydew kiwi lemon mango nectarine orange pear quince raspberry strawberry zucchini tangerine ugli fruit valencia orange watermelon xigua yellow passion fruit\n")

with open("./file.txt", "r") as file:
    words = file.read().split()
    last_word = max(words, key=str.lower)
    print("The last word alphabetically is:", last_word)
