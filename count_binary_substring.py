def count_binary_substring(s):
    prev = 0
    cur = 1
    ans = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            cur += 1
        else:
            pre = cur
            cur = 1
        if prev > cur:
            ans += 1

    return ans
