# O(n^2)
def longest_palindrome(s):
    def extend_palindrome(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left + 1 - 2

    if not s:
        return ""

    start, end = 0, 0
    for i in range(len(s)):
        len1 = extend_palindrome(s, i, i)
        len2 = extend_palindrome(s, i, i + 1)
        l = max(len1, len2)
        if l > end - start:
            start = i - (l - 1) // 2
            end = i + l // 2

    return s[start:end + 1]

print(longest_palindrome("babad"))
