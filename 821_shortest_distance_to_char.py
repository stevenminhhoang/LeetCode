def shortest_to_char(S, C):
    res = [0 if c == C else len(S) for c in S]
    for i in range(len(S) - 1):
        res[i + 1] = min(res[i + 1], res[i] + 1)
    for i in range(len(S) - 2, -1, -1):
        res[i] = min(res[i], res[i + 1] + 1)

    return res

print(shortest_to_char("loveleetcode", "e"))
