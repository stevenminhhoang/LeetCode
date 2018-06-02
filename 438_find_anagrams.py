
from collections import Counter

def find_anagrams(s, p):
    res = []
    k = len(p) - 1
    p_counter = Counter(p)
    s_counter = Counter(s[:k])
    for i in range(k, len(s)):
        s_counter[s[i]] += 1
        if s_counter == p_counter:
            res.append(i-k)
        s_counter[s[i-k]] -= 1
        if s_counter[s[i-k]] == 0:
            del s_counter[s[i-k]]

    return res





print(find_anagrams("cbaebabacd", "abc"))
print(find_anagrams("abab", "ab"))
