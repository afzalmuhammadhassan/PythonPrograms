def is_palindrome(s):
    def to_chars(s):
        ans = ''
        for c in s.lower():
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
    return is_pal(to_chars(s))

