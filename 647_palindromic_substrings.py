# O(n^2)
def palindromic_substrings(s):
    def extend_palindrome(s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        return count

    if not s:
        return 0

    ans = 0
    for i in range(len(s)):
        ans += extend_palindrome(s, i, i)
        ans += extend_palindrome(s, i ,i + 1)

    return ans


print(palindromic_substrings("abc"))
print(palindromic_substrings("aaa"))
