# O(m * n)
import collections
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
MAX = float('inf')

def print_matrix(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=' ')
        print()

def zero_one_matrix(matrix):
    distance = [[MAX for j in range(len(matrix[0]))] for i in range(len(matrix))]
    queue = collections.deque()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                distance[row][col] = 0
                queue.append((row, col))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < len(matrix) and 0 <= nc < len(matrix[0])):
                continue
            if distance[nr][nc] > distance[r][c] + 1:
                distance[nr][nc] = distance[r][c] + 1
                queue.append((nr, nc))

    return distance

matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]


print_matrix(zero_one_matrix(matrix))
