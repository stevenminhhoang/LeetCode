# O(n)
def findMode(self, root):
    def dfs(node):
        if not node:
            return
        count[node.val] += 1
        dfs(node.left)
        dfs(node.right)

    if not root:
        return []

    count = collections.Counter()
    dfs(root)
    max_val = max(count.values())
    return [k for k, v in count.items() if v == max_val]
