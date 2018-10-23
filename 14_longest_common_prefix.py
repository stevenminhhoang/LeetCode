# O(n)
# Space: O(1)
def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]

    return strs[0]

print(longestCommonPrefix(["flower","flow","flight"]))
