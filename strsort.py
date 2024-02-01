def strsort(s):
    words = s.split(' ')
    if words != None:
        sorted_str = []
        for word in words:
             sorted_str.append(''.join(sorted(word)))
    
    print(sorted_str)

if __name__ == '__main__':
    """
    print(strsort('cba'))
    print(strsort('bdac'))
    print(strsort('Tom Dick Harry'))
    """
    strsort('Tom Dick Harry')