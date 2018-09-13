# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(l, node):
            if not node:
                return -1
            left = dfs(l, node.left)
            right = dfs(l, node.right)
            level = 1 + max(left, right)
            if level == len(l):
                l.append([])
            l[level].append(node.val)
            node.left = None
            node.right = None
            return level

        res = []
        dfs(res, root)
        return res

            
