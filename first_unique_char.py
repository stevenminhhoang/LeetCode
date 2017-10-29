def firstUniqChar(s):
    letters = "abcdefghijklmnopqrstuvwxyz"
    index = [s.index(char) for char in letters if s.count(char) == 1]
    return min(index) if len(index) > 0 else -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("hhooaann"))
