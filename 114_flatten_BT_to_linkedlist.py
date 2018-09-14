# DFS Iterative
def flatten(self, root):
    if not root:
        return

    stack = []
    stack.append(root)
    prev = None
    while stack:
        curr = stack.pop()
        if prev:
            prev.right = curr
            prev.left = None
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

        prev = curr

# Recursive
def flatten(self, root):
    self.prev = None
    def dfs(node):
        if not node:
            return
        dfs(node.right)
        dfs(node.left)
        node.right = self.prev
        node.left = None
        self.prev = node

    dfs(root)
