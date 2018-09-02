def atoi(str):
    ls = list(str.strip())
    if len(ls) == 0:
        return 0

    sign = 1
    if ls[0] == '-':
        sign = -1

    if ls[0] in ('-', '+'):
        del ls[0]

    i = 0
    res = 0
    while i < len(ls) and ls[i].isdigit():
        res = res * 10 + ord(ls[i]) - ord("0")
        i += 1

    return max(-2**31, min(2**31 - 1, res * sign))

# print(atoi("4193 with words"))
print(atoi(" 42"))
