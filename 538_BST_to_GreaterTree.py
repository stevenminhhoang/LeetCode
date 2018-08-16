# Recursive
class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        self.convertBST(root.right)
        self.total += root.val
        root.val = self.total
        self.convertBST(root.left)

        return root

# Iterative
def convertBST(self, root):
    stack = []
    total = 0
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.right

        node = stack.pop()
        total += node.val
        node.val = total

        node = node.left

    return root
