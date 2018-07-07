def permutation(string):
    l = []
    backtrack(l, list(string), 0)
    return l

def backtrack(list, string, start):
    if start == len(string):
        list.append(''.join(string))

    for i in range(start, len(string)):
        string[i], string[start] = string[start], string[i]
        backtrack(list, string, start + 1)
        string[i], string[start] = string[start], string[i]


print(permutation("ABC"))
