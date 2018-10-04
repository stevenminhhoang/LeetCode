# O(n)
import collections
def length_longest_substring_k_distinct(s, k):
    count = collections.Counter()
    ans, length = "", 0
    start = 0
    counter = 0
    for end in range(len(s)):
        curr = s[end]
        count[curr] += 1
        if count[curr] == 1:
            counter += 1

        while counter > k:
            start_char = s[start]
            if start_char in count:
                count[start_char] -= 1
                if count[start_char] == 0:
                    counter -= 1

            start += 1

        if end - start + 1 > length:
            length = end - start + 1
            ans = s[start:end + 1]

    return ans

print(length_longest_substring_k_distinct("eceba", 2))
