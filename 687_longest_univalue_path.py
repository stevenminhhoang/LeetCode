# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left_arrow, right_arrow = 0, 0
            if node.left and node.left.val == node.val:
                left_arrow = left + 1
            if node.right and node.right.val == node.val:
                right_arrow = right + 1
            self.longest = max(self.longest, left_arrow + right_arrow)

            return max(left_arrow, right_arrow)

        dfs(root)
        return self.longest
