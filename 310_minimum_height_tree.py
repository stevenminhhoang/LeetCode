# O(n)
import collections
def min_height_tree(n, edges):
    if n <= 1:
        return [0]

    graph = {x: [] for x in range(n)}
    degrees = [0] * n
    for p in edges:
        degrees[p[0]] += 1
        degrees[p[1]] += 1
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])

    queue = collections.deque()
    res = []
    for i in range(n):
        if degrees[i] == 0:
            return res
        if degrees[i] == 1:
            queue.append(i)

    while queue:
        res = []
        size = len(queue)
        for i in range(size):
            curr = queue.popleft()
            res.append(curr)
            degrees[curr] -= 1

            for neighbor in graph[curr]:
                if degrees[neighbor] == 0:
                    continue
                if degrees[neighbor] == 2:
                    queue.append(neighbor)

                degrees[neighbor] -= 1

    return res

print(min_height_tree(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
