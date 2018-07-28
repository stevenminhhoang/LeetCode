# O(n) using hashmap
# def can_permute_palindrome(s):
#     if not s:
#         return True
#     dic = {}
#     count = 0
#     for char in s:
#         dic[char] = dic.get(char, 0) + 1
#
#     for key, val in dic.items():
#         if val % 2 != 0:
#             count += 1
#
#     return count <= 1
#
# print(can_permute_palindrome("carerac"))

# O(n) using Array

# def can_permute_palindrome(s):
#     count = 0
#     map = [0 for i in range(128)]
#     for char in s:
#         map[ord(char)] += 1
#
#     for i in range(len(map)):
#         count += map[i] % 2
#
#     return count <= 1
#
#
# print(can_permute_palindrome("carerac"))

# Single pass
def can_permute_palindrome(s):
    count = 0
    map = [0 for i in range(128)]
    for char in s:
        map[ord(char)] += 1
        if map[ord(char)] % 2 != 0:
            count += 1
        else:
            count -= 1

    return count <= 1

print(can_permute_palindrome("carerac"))
