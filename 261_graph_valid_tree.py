# O(V * E)
import collections
def valid_tree(n, edges):
    visited = set()
    graph = {i: set() for i in range(n)}
    for x, y in edges:
        graph[x].add(y)
        graph[y].add(x)

    queue = collections.deque()
    queue.append(0)
    while queue:
        curr = queue.popleft()
        if curr in visited:
            return False
        visited.add(curr)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                queue.append(neighbor)


    return len(visited) == n

print(valid_tree(5, [[0,1], [0,2], [0,3], [1,4]]))
