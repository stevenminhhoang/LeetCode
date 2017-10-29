def valid_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return is_palindrome(s[left+1:right]) or is_palindrome(s[left:right-1])

    return True

def is_palindrome(s):
    return s == s[::-1]

print(valid_palindrome("abcda"))
