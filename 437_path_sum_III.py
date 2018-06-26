# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def pathSumFrom(node, sum):
            if not node:
                return 0

            return int(node.val == sum) + pathSumFrom(node.left, sum - node.val) + pathSumFrom(node.right, sum - node.val)

        if not root:
            return 0

        return pathSumFrom(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
