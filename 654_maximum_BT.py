# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def max_index(nums, l, r):
            m_i = l
            for i in range(l, r + 1):
                if nums[m_i] < nums[i]:
                    m_i = i
            return m_i

        def max_tree(nums, l, r):
            if l > r:
                return None
            m = max_index(nums, l, r)
            root = TreeNode(nums[m])
            root.left = max_tree(nums, l, m - 1)
            root.right = max_tree(nums, m + 1, r)
            return root

        return max_tree(nums, 0, len(nums) - 1)
