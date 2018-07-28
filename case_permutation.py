def case_permutation(s):
    def backtrack(lis, temp, start, s):
        if start == len(s):
            lis.append(temp[:])
            return

        x = s[start]
        backtrack(lis, temp + x.upper(), start + 1, s)
        backtrack(lis, temp + x.lower(), start + 1, s)



    if not s:
        return []

    lis = []
    backtrack(lis, "", 0, s)
    return lis

print(case_permutation("abcd"))
