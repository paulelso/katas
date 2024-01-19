"""
Function that takes a list of words and returns the length of the shortest word,
the length of the longest word, and the average word length.
"""

def get_length(s):
    count, length, shortest, longest, average = 0, 0, 0, 0, 0
    for word in s:
        count += 1
        length += len(word)
        if shortest == 0:
            shortest = len(word)
        if len(word) < shortest:
            shortest = len(word)
        if len(word) > longest:
            longest = len(word)
    average = length / count
    return shortest, longest, average


if __name__ == '__main__':
    s = ["shortest", "longest", "average"]
    shortest, longest, average = get_length(s)
    print('Shortest word: {}'.format(shortest))
    print('Longest word: {}'.format(longest))
    print('Average word length: {:.2f}'.format(average))
