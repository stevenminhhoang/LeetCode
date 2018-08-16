def countUnivalSubtrees(self, root):
    def dfs(node):
        global count
        if not node:
            return True
        left = dfs(node.left)
        right = dfs(node.right)
        if left and right:
            if node.left and node.val != node.left.val:
                return False
            if node.right and node.val != node.right.val:
                return False

            count += 1
            return True

        return False

    global count
    count = 0
    dfs(root)
    return count
