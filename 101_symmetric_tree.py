# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # Recursive
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False

            return t1.val == t2.val and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

        return is_mirror(root, root)

    # BFS
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque()
        queue.append(root)
        queue.append(root)
        while queue:
            n1 = queue.popleft()
            n2 = queue.popleft()
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False

            queue.append(n1.left)
            queue.append(n2.right)
            queue.append(n1.right)
            queue.append(n2.left)

        return True
