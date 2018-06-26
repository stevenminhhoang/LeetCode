from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # BFS
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        dic = set()
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node and (k - node.val) in dic:
                    return True
            dic.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False

    # DFS
    def findTarget(self, root, k):
        def find(t, k, dic):
            if not t:
                return False
            if k - t.val in dic:
                return True
            dic.add(t.val)

            return find(t.left, k, dic) or find(t.right, k, dic)

        dic = set()
        return find(root, k, dic)

    # Two pointers
    def findTarget(self, root, k):
        def inorder(root, arr):
            if not root:
                return
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)

        arr = []
        inorder(root, arr)
        l, r = 0, len(arr) - 1
        while l < r:
            two_sum = arr[l] + arr[r]
            if two_sum == k :
                return True
            elif two_sum < k:
                l += 1
            else:
                r -= 1

        return False
