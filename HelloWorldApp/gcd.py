def gcditer(a, b):
    if b % a == 0:
        return a
    else:
        return gcditer((b % a), a)
