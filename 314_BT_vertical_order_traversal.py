# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        dic = collections.defaultdict(list)
        queue = collections.deque()
        cols = collections.deque()
        queue.append(root)
        cols.append(0)
        min_val, max_val = 0, 0
        while queue:
            node = queue.popleft()
            col = cols.popleft()
            dic[col].append(node.val)
            if node.left:
                queue.append(node.left)
                cols.append(col - 1)
                min_val = min(min_val, col - 1)
            if node.right:
                queue.append(node.right)
                cols.append(col + 1)
                max_val = max(max_val, col + 1)

        for i in range(min_val, max_val + 1):
            res.append(dic[i])

        return res





        
