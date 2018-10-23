"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        dummy = Node(0, None, None)
        self.prev = dummy
        def inorder(curr):
            if not curr:
                return

            inorder(curr.left)
            self.prev.right = curr
            curr.left = self.prev
            self.prev = curr
            inorder(curr.right)


        if not root:
            return

        inorder(root)
        self.prev.right = dummy.right
        dummy.right.left = self.prev

        return dummy.right
