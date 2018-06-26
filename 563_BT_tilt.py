# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0
        def traverse(root):
            if not root:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            self.tilt += abs(left - right)

            return left + right + root.val

        traverse(root)
        return self.tilt
