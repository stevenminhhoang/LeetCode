# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def trim(root):
            if not root:
                return None
            elif root.val < L:
                return trim(root.right)
            elif root.val > R:
                return trim(root.left)
            else:
                root.left = trim(root.left)
                root.right = trim(root.right)
                return root
        return trim(root)
