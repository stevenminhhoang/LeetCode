# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def dfs(node, i, sum_i, count):
            if not node:
                return
            if i < len(sum_i):
                sum_i[i] += node.val
                count[i] += 1
            else:
                sum_i[i] = node.val
                count[i] = 1.0

            dfs(node.left, i + 1, sum_i, count)
            dfs(node.right, i + 1, sum_i, count)

        res = {}
        count = {}
        ans = []
        dfs(root, 0, res, count)
        for i in range(len(res)):
            ans.append(res[i] / count[i])

        return ans
