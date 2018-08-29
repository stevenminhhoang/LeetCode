# O(n + m) n is number of edges, m is number of nodes
from collections import deque
def count_components(n, edges):
    # DFS
    def dfs(n, graph, visited):
        if visited[n]:
            return
        visited[n] = 1
        for x in graph[n]:
            dfs(x, graph, visited)

    visited = [0] * n
    graph = {x: [] for x in range(n)}
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    ans = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, graph, visited)
            ans += 1

    return ans

    # BFS
    visited = [0] * n
    graph = {x: [] for x in range(n)}
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    count = 0
    queue = deque()
    for i in range(n):
        if not visited[i]:
            queue.append(i)
            visited[index] = 1
            while queue:
                index = queue.popleft()
                for neighbor in graph[index]:
                    if not visited[neighbor]:
                        visited[neighbor] = 1
                        queue.append(neighbor)
            count += 1

    return count


print(count_components(5, [[0, 1], [1, 2], [3, 4]]))
