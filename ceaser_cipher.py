def cipher_text(text, key):
    encrypted_text = ""
    for c in text:
        if c.isupper():
            new_position = ord(c) + key
            if new_position > ord('Z'):
                new_position = new_position - ord('Z') + ord('A') - 1
        elif c.islower():
            new_position = ord(c) + key
            if new_position > ord('z'):
                new_position = new_position - ord('z') + ord('a') - 1
        else:
            new_position = ord(c)
        encrypted_text += chr(new_position)
    return encrypted_text


if __name__ == "__main__":
    text = input("Enter text to encrypt: ")
    key = int(input("Key: "))
    print(cipher_text(text, key))