def reverse_integer(x):
    ans = 0
    a = abs(x)
    while a != 0:
        digit = a % 10
        ans = ans * 10 + digit
        a = a // 10

    if x > 0 and ans < 2 ** 31:
        return ans
    elif x < 0 and ans <= 2 ** 31:
        return -ans
    else:
        return 0

    return ans


print(reverse_integer(-123))
