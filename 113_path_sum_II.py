# DFS Iterative
def pathSum(self, root, s):
    if not root:
        return []
    stack = []
    stack.append((root, [root.val]))
    res = []
    while stack:
        node, temp = stack.pop()
        if not node.left and not node.right and sum(temp) == s:
           res.append(temp)
        if node.left:
            stack.append((node.left, temp + [node.left.val]))
        if node.right:
            stack.append((node.right, temp + [node.right.val]))

    return res

# DFS Recursive
def pathSum(self, root, s):
    def dfs(res, temp, root, s):
        if not root:
            return
        if not root.left and not root.right and s == root.val:
            res.append(temp + [root.val])
        if root.left:
            dfs(res, temp + [root.val], root.left, s - root.val)
        if root.right:
            dfs(res, temp + [root.val], root.right, s - root.val)

    if not root:
        return []

    res = []
    dfs(res, [], root, s)
    return res

# BFS
def pathSum(self, root, s):
    if not root:
        return []

    queue = collections.deque()
    res = []
    queue.append((root, root.val, [root.val]))
    while queue:
        node, val, temp = queue.popleft()
        if not node.left and not node.right and val == s:
            res.append(temp)
        if node.left:
            queue.append((node.left, val + node.left.val, temp + [node.left.val]))
        if node.right:
            queue.append((node.right, val + node.right.val, temp + [node.right.val]))

    return res
