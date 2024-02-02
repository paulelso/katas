# Description: Function takes a string and returns a string  
# with the letters in each word sorted alphabetically.
# String with spaces is split into a list of words. The words are
# sorted alphabetically and joined into a string with a comma and space.
def strsort(s):
    words = s.split(' ')
    sorted_lst = []
    for word in words:
        sorted_lst.append(''.join(sorted(word)))
    return ', '.join(sorted_lst)    
    

if __name__ == '__main__':
    print(strsort('cba'))
    print(strsort('bdac'))
    print(strsort('Tom Dick Harry'))
    print(strsort('Tom Dick Harry'))