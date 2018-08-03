# O(2^n * n)
def letter_case_permutation(S):
    def backtrack(lis, temp, start, S):
        if start == len(S):
            lis.append("".join(temp[:]))
            return
        x = S[start]
        if x.isdigit():
            temp.append(x)
            backtrack(lis, temp, start + 1, S)
            temp.pop()
        else:
            temp.append(x.upper())
            backtrack(lis, temp, start + 1, S)
            temp.pop()

            temp.append(x.lower())
            backtrack(lis, temp, start + 1, S)
            temp.pop()

    lis = []
    backtrack(lis, [], 0, S)
    return lis

print(letter_case_permutation("a1b2"))

def letter_case_permutation(S):
    def backtrack(lis, temp, start, S):
        if start == len(S):
            lis.append(temp)
            return
        x = S[start]
        if x.isdigit():
            backtrack(lis, temp + x, start + 1, S)
        else:
            backtrack(lis, temp + x.upper(), start + 1, S)
            backtrack(lis, temp + x.lower(), start + 1, S)

    lis = []
    backtrack(lis, "", 0, S)
    return lis

print(letter_case_permutation("a1b2"))
