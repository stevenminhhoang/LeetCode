def isAnagram(self, s, t):
    count = [0] * 26
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for char in count:
        if char != 0:
            return False

    return True
