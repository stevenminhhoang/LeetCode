# O(n)
import collections
def permutation_in_string(s1, s2):
    count = collections.Counter(s1)
    res = ""
    start, end = 0, 0
    counter = len(count)
    while end < len(s2):
        curr = s2[end]
        if curr in count:
            count[curr] -= 1
            if count[curr] == 0:
                counter -= 1

        end += 1

        while counter == 0:
            if end - start == len(s1):
                res = s2[start:end]
                print(res)
                return True

            start_char = s2[start]
            if start_char in count:
                count[start_char] += 1
                if count[start_char] > 0:
                    counter += 1

            start += 1

    return False


print(permutation_in_string("ab", "eidbaooo"))
