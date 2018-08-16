
def sumOfLeftLeaves(self, root):
    if not root:
        return 0
    if root.left and not root.left.left and not root.left.right:
        return root.left.val + self.sumOfLeftLeaves(root.right)

    return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

def sumOfLeftLeaves(self, root):
    total = [0]
    def dfs(node):
        if not node:
            return 0
        if node.left and not node.left.left and not node.left.right:
            total[0] += node.left.val

        left = dfs(node.left)
        right = dfs(node.right)

        return left + right

    dfs(root)
    return total[0]
