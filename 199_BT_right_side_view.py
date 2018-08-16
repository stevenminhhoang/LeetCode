from collections import deque

# BFS
def rightSideView(self, root):
    if not root:
        return []
    ans = []
    rightmost_node = {}
    queue = deque()
    queue.append((root, 0))
    while queue:
        size = len(queue)
        for i in range(size):
            node, depth = queue.popleft()
            rightmost_node[depth] = node.val
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

    for depth in rightmost_node:
        ans.append(rightmost_node[depth])

    return ans

# DFS
def rightSideView(self, root):
    def dfs(res, node, level, dic):
        if not node:
            return
        if len(res) == level:
            res.append(node.val)


        dfs(res, node.right, level + 1, dic)
        dfs(res, node.left, level + 1, dic)


    res = []
    dic = {}
    dfs(res, root, 0, dic)
    return res

# DFS with Hashmap
def rightSideView(self, root):
    if not root:
        return []

    res = []
    dic = {}
    stack = []
    stack.append((root, 0))
    while stack:
        node, depth = stack.pop()
        dic[depth] = node.val
        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))

    for depth in dic:
        res.append(dic[depth])

    return res
