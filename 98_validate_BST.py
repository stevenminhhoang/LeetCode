# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        pre = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if pre and root.val <= pre.val:
                return False

            pre = root
            root = root.right

        return True
