def add_strings(num1, num2):
    res = []
    carry = 0
    i, j = len(num1) - 1, len(num2) - 1
    while i >= 0 or j >= 0:
        x = ord(num1[i]) - ord('0') if i >= 0 else 0
        y = ord(num2[j]) - ord('0') if j >= 0 else 0
        s = x + y + carry
        carry = s // 10
        res.append(s % 10)
        i -= 1
        j -= 1

    if carry == 1:
        res.append(1)

    return "".join(map(str, res[::-1]))

print(add_strings("99", "101"))
