# BFS
# O(V + E)
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


    for i in range(n):
        if i not in visited:
            return False

    return True

# DFS
# O(V + E)
def validTree(n, edges):
    def is_cyclic(curr, parent, graph, visited):
        visited[curr] = True
        for i in graph[curr]:
            if not visited[i]:
                if is_cyclic(i, curr, graph, visited):
                    return True
            elif visited[i] and i != parent:
                return True

        return False

    graph = {x: [] for x in range(n)}
    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)


    visited = [False] * n
    if is_cyclic(0, -1, graph, visited):
        return False

    for i in range(n):
        if not visited[i]:
            return False

    return True

print(valid_tree(5, [[0,1], [0,2], [0,3], [1,4]]))
