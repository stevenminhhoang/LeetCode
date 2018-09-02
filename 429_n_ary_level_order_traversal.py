"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                node = queue.popleft()
                temp.append(node.val)
                for neighbor in node.children:
                    queue.append(neighbor)

            res.append(temp)

        return res
