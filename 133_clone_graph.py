# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # BFS
    def cloneGraph(self, node):
        if not node:
            return

        new_node = UndirectedGraphNode(node.label)
        visited = {}
        visited[new_node.label] = new_node
        queue = collections.deque()
        queue.append(node)

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor.label not in visited:
                    neighbor_node = UndirectedGraphNode(neighbor.label)
                    visited[neighbor.label] = neighbor_node
                    queue.append(neighbor)

                visited[n.label].neighbors.append(visited[neighbor.label])

        return new_node

# Recursive DFS:
def cloneGraph(self, node):
    if not node:
        return

    dic = {}
    node_copy = UndirectedGraphNode(node.label)
    dic[node] = node_copy
    self.dfs(node, dic)
    return node_copy

def dfs(self, node, dic):
    for nei in node.neighbors:
        if nei not in dic:
            nei_copy = UndirectedGraphNode(nei.label)
            dic[nei] = nei_copy
            self.dfs(nei, dic)

        dic[node].neighbors.append(dic[nei])
