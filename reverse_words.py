# Description: Function that takes a sentence as input and 
# returns the sentence with the order of words reversed. 
# For example, "Hello World" should become "World Hello".
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


if __name__ == "__main__":
    print(reverse_sentence("Hello World"))
    print(reverse_sentence("Hello! My name is Paulo Sousa."))