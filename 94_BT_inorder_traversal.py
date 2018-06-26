# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            ans.append(node.val)
            root = node.right
        return ans
