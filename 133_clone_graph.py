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
