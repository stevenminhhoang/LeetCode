from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # Recursion
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

    # BFS
    def invertTree(self, root):
        queue = deque()
        if not root:
            return
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)

        return root

    # DFS
    def invertTree(self, root):
        if not root:
            return
        left = root.left
        right = root.right
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)

        return root
