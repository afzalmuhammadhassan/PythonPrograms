def count_number_of_string(s):
    ch = ''
    num = 0
    for i in s:
        ch += i
        if len(ch) == 3 and ch == 'bob':
            num += 1
            ch = i
        elif len(ch) == 3:
            if ch[1:] == 'bo':
                ch = 'bo'
            else:
                ch = i
    return num