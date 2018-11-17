# O(N^2)
import collections
def redundant_connection(edges):
    def dfs(curr, end, graph, visited):
        if curr == end:
            return True
        if curr in visited:
            return False

        visited.add(curr)
        for nei in graph[curr]:
            if dfs(nei, end, graph, visited):
                return True

    graph = collections.defaultdict(list)
    for u, v in edges:
        visited = set()
        if u in graph and v in graph and dfs(u, v, graph, visited):
            return u, v

        graph[u].append(v)
        graph[v].append(u)


print(redundant_connection([[1,2], [1,3], [2,3]]))
