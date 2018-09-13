def romanToInt(s):
    dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    res = 0
    for i in range(len(s) - 1):
        if dic[s[i + 1]] > dic[s[i]]:
            res -= dic[s[i]]
        else:
            res += dic[s[i]]

    res += dic[s[-1]]

    return res
