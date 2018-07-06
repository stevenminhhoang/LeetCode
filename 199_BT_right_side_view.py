from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        rightmost_node = {}
        queue = deque()
        queue.append((root, 0))
        while queue:
            size = len(queue)
            for i in range(size):
                node, depth = queue.popleft()
                rightmost_node[depth] = node.val
                if node.left:
                    queue.append((node.left, depth + 1))
                if node.right:
                    queue.append((node.right, depth + 1))

        for depth in rightmost_node:
            ans.append(rightmost_node[depth])

        return ans
