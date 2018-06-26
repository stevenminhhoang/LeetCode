# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        return None if root.val == 0 and not root.left and not root.right else root
