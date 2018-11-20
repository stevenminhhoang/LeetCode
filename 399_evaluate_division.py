# O(E * Q) E is number of equations(edges), Q is number of queries
import collections
def evaluate_division(equations, values, queries):
    def dfs(curr, end, visited, total):
        if curr in visited or curr not in graph:
            return -1.0
        if curr == end:
            return total

        visited.add(curr)
        for nei, d in graph[curr]:
            temp = dfs(nei, end, visited, total * d)
            if temp != -1:
                return temp

        return -1.0

    # def bfs(start, end):
    #     queue = collections.deque()
    #     queue.append((start, 1))
    #     visited = set()
    #     while queue:
    #         node, d = queue.popleft()
    #         if node not in graph:
    #             continue
    #         if node == end:
    #             return d * 1.0
    #         for nei, d2 in graph[node]:
    #             if nei not in visited:
    #                 visited.add(nei)
    #                 queue.append((nei, d * d2))
    #
    #     return -1.0

    res = []
    graph = collections.defaultdict(list)
    for i in range(len(equations)):
        u = equations[i][0]
        v = equations[i][1]
        graph[u].append((v, values[i]))
        graph[v].append((u, 1 / values[i]))

    for query in queries:
        res.append(dfs(query[0], query[1], set(), 1.0))

    return res



equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(evaluate_division(equations, values, queries))
