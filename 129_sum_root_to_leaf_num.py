# DFS Recursive
def sumNumbers(self, root):
    def dfs(res, node, val):
        if not node:
            return

        dfs(res, node.left, val * 10 + node.val)
        dfs(res, node.right, val * 10 + node.val)

        if not node.left and not node.right:
            res[0] += val * 10 + node.val

    res = [0]
    dfs(res, root, 0)
    return res[0]

# BFS
def sumNumbers(self, root):
    if not root:
        return 0

    queue = collections.deque([(root, root.val)])
    res = 0
    while queue:
        node, val = queue.popleft()
        if not node.left and not node.right:
            res += val
        if node.left:
            queue.append((node.left, val * 10 + node.left.val))
        if node.right:
            queue.append((node.right, val * 10 + node.right.val))

    return res

# DFS
def sumNumbers(self, root):
    if not root:
        return 0

    stack = []
    res = 0
    stack.append((root, root.val))
    while stack:
        node, val = stack.pop()
        if not node.left and not node.right:
            res += val
        if node.right:
            stack.append((node.right, val * 10 + node.right.val))
        if node.left:
            stack.append((node.left, val * 10 + node.left.val))

    return res
