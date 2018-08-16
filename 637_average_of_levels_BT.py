# DFS
def averageOfLevels(self, root):
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

# BFS
 def averageOfLevels(self, root):
    if not root:
        return []

    queue = collections.deque([root])
    res = []
    while queue:
        total = 0
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            total += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(total * 1.0 / size)

    return res
