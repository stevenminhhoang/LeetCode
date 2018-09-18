# O(n)
import collections
def characterReplacement(s, k):
    count = collections.Counter()
    start = 0
    length = 0
    ans = ""
    max_count = 0
    for end in range(len(s)):
        curr = s[end]
        count[curr] += 1
        max_count = max(max_count, count[curr])

        while end - start + 1 - max_count > k:
            start_char = s[start]
            count[start_char] -= 1
            start += 1

        if end - start + 1 > length:
            length = end - start + 1
            ans = s[start:end + 1]

    print(ans)
    return length

print(characterReplacement("AABABBA", 1))
