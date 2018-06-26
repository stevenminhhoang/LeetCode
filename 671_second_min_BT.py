# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        set_node = set()
        def dfs(node):
            if not node:
                return
            set_node.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        min_val, ans = root.val, float('inf')
        for v in set_node:
            if min_val < v < ans:
                ans = v

        return ans if ans < float('inf') else -1
