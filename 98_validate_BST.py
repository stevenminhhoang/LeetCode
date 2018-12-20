# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Iterative
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
            if pre and pre.val >= root.val:
                return False

            pre = root
            root = root.right

        return True

    # Recursive
     def isValidBST(self, root):
        def isValid(node, minVal, maxVal):
            if not node:
                return True
            if node.val <= minVal or node.val >= maxVal:
                return False

            return isValid(node.left, minVal, node.val) and isValid(node.right, node.val, maxVal)

        return isValid(root, float("-inf"), float("inf"))
