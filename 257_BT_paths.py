# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.ans = []
        if not root:
            return []

        def dfs(node, ls):
            if node:
                if not node.left and not node.right:
                    self.ans.append(ls + str(node.val))

                dfs(node.left, ls + str(node.val) + "->")
                dfs(node.right, ls + str(node.val) + "->")


        dfs(root, "")
        return self.ans
