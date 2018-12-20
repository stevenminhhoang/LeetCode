def title_to_number(s):
    res = 0
    for i in range(len(s)):
        res = res * 26 + ord(s[i]) - ord("A") + 1

    return res

print(title_to_number("ZY"))
