def find_longest_alphabetic_string(s):
    ch = '\0'
    l_str = ''
    for i in s:
        if ch[-1] <= i:
           ch += i
        else:
            if len(l_str) < len(ch):
                l_str = ch
                print(l_str)
            ch = i
    if len(l_str) < len(ch):
        l_str = ch
    return l_str