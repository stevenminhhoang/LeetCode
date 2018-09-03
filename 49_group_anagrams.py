# O(n * k * log(k)) k is max length of a string in strs
import collections
# def group_anagrams(strs):
#     dic = collections.defaultdict(list)
#     for s in strs:
#         dic[tuple(sorted(s))].append(s)
#
#     res = []
#     for val in dic.values():
#         res.append(val)
#
#     return res


# O(n * k)
def group_anagrams(strs):
    dic = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1

        dic[tuple(count)].append(s)

    return [x for x in dic.values()]


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
