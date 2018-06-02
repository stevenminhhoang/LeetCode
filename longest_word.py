# Brute Force
# def longest_word(words):
#     ans = ""
#     word_set = set(words)
#     for word in words:
#         if len(word) > len(ans) or len(word) == len(ans) and word < ans:
#             if all([word[:k] in word_set for k in range(1,len(word))]):
#                 ans = word
#
#     return ans
#
#
# print(longest_word(["w","wo","wor","worl", "world", "wor"]))

# Using Trie + DFS
def longest_word(words):
    
