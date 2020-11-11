def binary_for_decimal(x):
    p = 0
    while ((2 ** p) * x) % 1 != 0:
        print('Remainder =', str((2 ** p) * x - int((2 ** p) * x)))
        p += 1
    num = int((2 ** p) * x)
    result = ''
    if num == 0:
        result = 0
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    print('For Loop Itrations', str(p - len(result)))
    for i in range(p - len(result)):
        result = '0' + result
    res1 = result[0:-p]
    print('res1: ', res1)
    res2 = result[-p:]
    print('res2: ', res2)
    result = res1 + '.' + res2
    return result
