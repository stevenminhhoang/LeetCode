def plus(s):
    def backtrack(res, temp, start, s):
        if start == len(s) - 1:
            res.append(temp + s[start])
            return

        backtrack(res, temp + s[start], start + 1, s)
        backtrack(res, temp + s[start] + '+', start + 1, s)

    res = []
    backtrack(res, "", 0, s)
    return res


print(plus("123"))
