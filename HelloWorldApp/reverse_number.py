def reverse_number(number):
    num_str = str(number)
    m = len(num_str) / 2
    i = 1
    result = num_str[0]
    while i <= m:
        if i < m:
            result += num_str[-i]
        result += num_str[i]
        i += 1
    result = int(result)
    return  result
