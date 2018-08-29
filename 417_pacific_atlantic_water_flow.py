# O(m * n)
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
import collections

def print_matrix(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=' ')
        print()

def water_flow(matrix):
    def bfs(matrix, visited, queue):
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if not (0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and visited[nr][nc] == False and matrix[nr][nc] >= matrix[r][c]):
                    continue

                visited[nr][nc] = True
                queue.append((nr, nc))

    if not matrix:
        return
    pacific = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
    atlantic = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
    p_queue = collections.deque()
    a_queue = collections.deque()
    for i in range(len(matrix)):
        p_queue.append((i, 0))
        pacific[i][0] = True
        a_queue.append((i, len(matrix[0]) - 1))
        atlantic[i][len(matrix[0]) - 1] = True
    for j in range(len(matrix[0])):
        p_queue.append((0, j))
        pacific[0][j] = True
        a_queue.append((len(matrix) - 1, j))
        atlantic[len(matrix) - 1][j] = True

    bfs(matrix, pacific, p_queue)
    bfs(matrix, atlantic, a_queue)

    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if pacific[i][j] and atlantic[i][j]:
                res.append([i, j])

    return res


grid = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(water_flow(grid))
