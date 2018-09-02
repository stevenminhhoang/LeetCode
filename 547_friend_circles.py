import collections
# DFS
def findCircleNum(self, M):
    def dfs(M, visited, i):
        for j in range(len(M)):
            if not visited[j] and M[i][j] == 1:
                visited[j] = 1
                dfs(M, visited, j)


    visited = [0] * len(M)
    count = 0
    for i in range(len(M)):
        if not visited[i]:
            count += 1
            dfs(M, visited, i)

        return count

# BFS
def friend_circles(M):
    visited = [0] * len(M)
    count = 0
    queue = collections.deque()
    for i in range(len(M)):
        if not visited[i]:
            queue.append(i)
            while queue:
                curr = queue.popleft()
                visited[curr] = 1
                for j in range(len(M)):
                    if visited[j] == 0 and M[curr][j] == 1:
                        queue.append(j)

            count += 1

    return count
