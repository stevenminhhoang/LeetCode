def leafSimilar(self, root1, root2):
    def dfs(res, root):
        if not root:
            return
        if not root.left and not root.right:
            res.append(root.val)

        dfs(res, root.left)
        dfs(res, root.right)



    res1, res2 = [], []
    dfs(res1, root1)
    dfs(res2, root2)
    return res1 == res2
