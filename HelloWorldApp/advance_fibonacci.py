from datetime import datetime
def fib_sep(num, d):
    global counter
    counter += 1
    if num in d:
        return d[num]
    else:
        ans = fib_sep(num-1, d) + fib_sep(num-2, d)
        d[num] = ans
        return ans

def fib(num):
    global  counter
    counter += 1
    if num <= 1 :
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
