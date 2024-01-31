def ubbi_dubbi(word):
    new_word = ''
    for letter in word:
        if letter.lower() in 'aeiou':
            new_word += 'ub' + letter
        else:
            new_word += letter
    return new_word


if __name__ == '__main__':
    print(ubbi_dubbi('python'))
    print(ubbi_dubbi('code'))
    print(ubbi_dubbi('program'))
    print(ubbi_dubbi('octopus'))
    print(ubbi_dubbi('milk'))