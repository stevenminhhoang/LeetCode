# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def pathSumFrom(node, sum):
            if not node:
                return False

            if not node.left and not node.right and sum - node.val == 0:
                return True

            return pathSumFrom(node.left, sum - node.val) or pathSumFrom(node.right, sum - node.val)

        return pathSumFrom(root, sum)
