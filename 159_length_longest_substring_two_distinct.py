# O(n)
import collections
def length_of_longest_substring_two_distinct(s):
    if not s:
        return 0

    ans = ""
    length = 0
    start, end = 0, 0
    count = collections.Counter()
    counter = 0
    while end < len(s):
        curr = s[end]
        count[curr] += 1
        if count[curr] == 1:
            counter += 1

        end += 1

        while counter > 2:
            start_char = s[start]
            if start_char in count:
                count[start_char] -= 1
                if count[start_char] == 0:
                    counter -= 1

            start += 1

        if end - start > length:
            length = end - start
            ans = s[start:end]

    return ans

print(length_of_longest_substring_two_distinct("eceba"))
