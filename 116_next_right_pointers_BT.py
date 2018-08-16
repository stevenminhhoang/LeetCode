def connect(self, root):
    if not root:
        return

    queue = collections.deque()
    queue.append(root)
    while queue:
        length = len(queue)
        prev = None
        for i in range(length):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if prev:
                prev.next = node

            prev = node
