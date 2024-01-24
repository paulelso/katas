# Description: Function that performs basic string compression.
# For example, the string "aabcccccaaa" would become "a2b1c5a3"
def string_compression(s):
    compressed_string = ""
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            compressed_string += s[i] + str(count)
            count = 1
    compressed_string += s[-1] + str(count)
    return compressed_string


if __name__ == "__main__":
    print(string_compression("aabcccccaaa"))