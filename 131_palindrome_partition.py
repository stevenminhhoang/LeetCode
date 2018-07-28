# O(2^n * n)
def palindrome_partition(s):
    def is_palindrome(s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

    def backtrack(lis, temp, start, s):
        if start == len(s):
            lis.append(temp[:])
        else:
            for i in range(start, len(s)):
                if is_palindrome(s, start, i):
                    temp.append(s[start:i + 1])
                    backtrack(lis, temp, i + 1, s)
                    temp.pop()

    if not s:
        return []

    lis = []
    backtrack(lis, [], 0, s)
    return lis


print(palindrome_partition("aab"))
