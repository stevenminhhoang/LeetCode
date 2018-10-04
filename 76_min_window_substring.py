# O(n)
import collections
def min_window_substring(s, t):
    count = collections.Counter()
    for char in t:
        count[char] += 1

    start = 0
    end = 0
    counter = len(count)
    length = float('inf')
    ans = ""

    while end < len(s):
        end_char = s[end]
        if end_char in count:
            count[end_char] -= 1
            if count[end_char] == 0:
                counter -= 1

        end += 1

        while counter == 0:
            if end - start < length:
                length = end - start
                ans = s[start:end]

            start_char = s[start]
            if start_char in count:
                count[start_char] += 1
                if count[start_char] > 0:
                    counter += 1

            start += 1

    return ans

print(min_window_substring("ADOBECODEBANC", "ABC"))
print(min_window_substring("cabwefgewcwaefgcf","cae"))
