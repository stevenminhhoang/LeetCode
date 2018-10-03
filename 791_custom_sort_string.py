import collections
def custom_sort_string(S, T):
    res = []
    countT = collections.Counter(T)
    setS = set(S)
    for char in S:
        res.append(char * countT[char])

    for char in T:
        if char not in setS:
            res.append(char)

    return "".join(res)

print(custom_sort_string("cba", "abcd"))
