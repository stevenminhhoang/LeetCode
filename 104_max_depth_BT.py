# Recursive
def maxDepth(self, root):
    if not root:
        return 0

    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Level-order DFS
def maxDepth(self, root):
    if not root:
        return 0

    stack = []
    count = 0
    stack.append(root)
    while stack:
        temp = []
        while stack:
            node = stack.pop()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        stack = temp
        count += 1

    return count

# Level-order BFS
def maxDepth(self, root):
    if not root:
        return 0

    queue = collections.deque()
    queue.append(root)
    count = 0
    while queue:
        temp = collections.deque()
        while queue:
            node = queue.popleft()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)

        queue = temp
        count += 1

    return count
