# def is_palindrome(s):
#     if len(s) == 0:
#         return True
#     s = s.lower()
#     char_string = [l for l in s if l.isalnum()]
#     return char_string == char_string[::-1]

# using two-pointer:
def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
            continue
        else:
            return False
    return True


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
