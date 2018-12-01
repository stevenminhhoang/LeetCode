# O(N)
def min_distance(root):
    def dfs(node):
        if not node:
            return

        dfs(node.left)
        self.ans = min(self.ans, node.val - self.prev)
        self.prev = node.val
        dfs(node.right)

    self.prev = float("-inf")
    self.ans = float("inf")
    dfs(root)
    return self.ans
