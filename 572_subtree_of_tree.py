# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def same_tree(t1 , t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False

            return t1.val == t2.val and same_tree(t1.left, t2.left) and same_tree(t1.right, t2.right)

        if same_tree(s, t):
            return True
        if not s:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
