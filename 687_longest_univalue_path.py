def longestUnivaluePath(self, root):
    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        left_arrow, right_arrow = 0, 0
        if node.left and node.left.val == node.val:
            left_arrow += left + 1
        if node.right and node.right.val == node.val:
            right_arrow += right + 1

        longest[0] = max(longest[0], left_arrow + right_arrow)

        return max(left_arrow, right_arrow)



    longest = [0]
    dfs(root)
    return longest[0]
