# O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        graph = collections.defaultdict(list)
        def dfs(node, parent):
            if parent:
                graph[node].append(parent)
            if node.left:
                graph[node].append(node.left)
                dfs(node.left, node)
            if node.right:
                graph[node].append(node.right)
                dfs(node.right, node)


        res = []
        dfs(root, None)
        queue = collections.deque()
        visited = set()
        queue.append((target, 0))
        visited.add(target)
        while queue:
            node, distance = queue.popleft()
            if distance == K:
                res.append(node.val)
            if distance > K:
                break
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append((next_node, distance + 1))

        return res
