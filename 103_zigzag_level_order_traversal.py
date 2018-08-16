def zigzagLevelOrder(self, root):
    if not root:
        return []

    queue = collections.deque()
    res = []
    queue.append((root, 0))
    while queue:
        node, level = queue.popleft()
        if node:
            if level == len(res):
                res.append([])
            if level % 2 == 0:
                res[level].insert(0, node.val)
            else:
                res[level].append(node.val)

            queue.appendleft((node.left, level + 1))
            queue.appendleft((node.right, level + 1))

    return res
