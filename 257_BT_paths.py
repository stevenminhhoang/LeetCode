# Recursive
def binaryTreePaths(self, root):
    if not root:
        return []

    def dfs(root, res, temp):
        if not root.left and not root.right:
            res.append(temp + str(root.val))
            return res
        if root.left:
            dfs(root.left, res, temp + str(root.val) + "->")
        if root.right:
            dfs(root.right, res, temp + str(root.val) + "->")

    res = []
    dfs(root, res, "")
    return res

# BFS
def binaryTreePaths(self, root):
    if not root:
        return []

    res = []
    queue = collections.deque()
    queue.append((root, ""))
    while queue:
        node, temp = queue.popleft()
        if not node.left and not node.right:
            res.append(temp + str(node.val))
        if node.left:
            queue.append((node.left, temp + str(node.val) + "->"))
        if node.right:
            queue.append((node.right, temp + str(node.val) + "->"))

    return res



# DFS
def binaryTreePaths(self, root):
    if not root:
        return []

    stack = []
    res = []
    stack.append((root, ""))
    while stack:
        node, temp = stack.pop()
        if not node.left and not node.right:
            res.append(temp + str(node.val))
        if node.right:
            stack.append((node.right, temp + str(node.val) + "->"))
        if node.left:
            stack.append((node.left, temp + str(node.val) + "->"))

    return res
