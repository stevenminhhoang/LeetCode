# O(n)
import collections
def find_anagrams(s, p):
    if not s or len(s) < len(p):
        return []
    count = collections.Counter()
    start, end = 0, 0
    res = []
    for char in p:
        count[char] += 1

    counter = len(count)



    while end < len(s):
        end_char = s[end]
        if end_char in count:
            count[end_char] -= 1
            if count[end_char] == 0:
                counter -= 1

        end += 1

        while counter == 0:
            if end - start == len(p):
                res.append(start)

            start_char = s[start]
            if start_char in count:
                count[start_char] += 1
                if count[start_char] > 0:
                    counter += 1

            start += 1

    return res

print(find_anagrams("cbaebabacd", "abc"))
