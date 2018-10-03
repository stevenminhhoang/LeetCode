# O(n * 2^n) BFS
import collections
# def remove_invalid_parentheses(s):
#     def valid(s):
#         count = 0
#         for char in s:
#             if char == "(":
#                 count += 1
#             if char == ")":
#                 if count == 0:
#                     return False
#                 count -= 1
#
#         return count == 0
#
#     if not s:
#         return []
#
#     res = []
#     queue = collections.deque()
#     visited = set()
#     found = False
#     queue.append(s)
#     visited.add(s)
#     while queue:
#         string = queue.popleft()
#         if valid(string):
#             res.append(string)
#             found = True
#
#         if found:
#             continue
#
#         for i in range(len(string)):
#             if string[i] != "(" and string[i] != ")":
#                 continue
#             t = string[:i] + string[i+1:]
#             if t not in visited:
#                 visited.add(t)
#                 queue.append(t)
#
#     return res


#O(n^2) DFS
def remove_invalid_parentheses(s):
    res = []
    dfs(res, [])



print(remove_invalid_parentheses("()())()"))
