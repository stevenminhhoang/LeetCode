def add_binary(a, b):
    res, i, j, s = [], len(a) - 1, len(b) - 1, 0
    while i >= 0 or j >= 0 or s:
        if i >= 0:
            s += int(a[i])
            i -= 1
        if j >= 0:
            s += int(b[j])
            j -= 1

        res.append(str(s % 2))
        s /= 2

    return "".join(res[::-1])



print(add_binary("11", "1"))
