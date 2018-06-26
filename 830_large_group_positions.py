def large_group_positions(S):
    ans = []
    start, end = 0, 0
    for i in range(1, len(S)):
        if S[i] != S[i - 1]:
            end = i - 1
            if end - start >= 2:
                ans.append([start, end])
            start = i
    if len(S) - 1 - start >= 2:
        ans.append([start, len(S) - 1])

    return ans

print(large_group_positions("abbxxxxzzy"))
print(large_group_positions("abc"))
print(large_group_positions("abcdddeeeeaabbbcd"))
print(large_group_positions("aaa"))
