# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        dic = {}

        def dfs(node):
            if not node:
                return
            dic[node.val] = abs(node.val - target)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        ans = 0
        min_diff = float('inf')
        for key in dic:
            if dic[key] < min_diff:
                min_diff = dic[key]
                ans = key

        return ans

            
