# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        result = str(t.val)
        if t.left:
            result += "(" + self.tree2str(t.left) + ")"
            if t.right:
                result += "(" + self.tree2str(t.right) + ")"
        elif t.right:
            result += "()" + "(" + self.tree2str(t.right) + ")"

        return result

        # Pythonic
        if not t:
            return ""
        left = "{}".format(self.tree2str(t.left)) if (t.left or t.right) else ""
        right = "{}".format(self.tree2str(t.right) if t.right) else ""

        return "{}{}{}".format(t.val, left, right) 
