# O(log10(n))
def palindrome_number(x):
    if x == 0:
        return True
    if x < 0 or x % 10 == 0:
        return False


    revert = 0
    while x > revert:
        revert = revert * 10 + x % 10
        x = x // 10

    return x == revert or x == revert // 10

print(palindrome_number(121))
