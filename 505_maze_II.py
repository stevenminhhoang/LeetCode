# O(m * n * max(m, n))
import collections
MAX = float('inf')
dr = [1,0,-1,0]
dc = [0,1,0,-1]

def print_matrix(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=' ')
        print()

def maze_II(maze, start, end):
    queue = collections.deque()
    distance = [[MAX for j in range(len(maze[0]))] for i in range(len(maze))]
    distance[start[0]][start[1]] = 0
    queue.append((start[0], start[1]))
    while queue:
        row, col = queue.popleft()
        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]
            count = 0
            while (0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] == 0):
                nr += dr[i]
                nc += dc[i]
                count += 1
            if distance[row][col] + count < distance[nr - dr[i]][nc - dc[i]]:
                distance[nr - dr[i]][nc - dc[i]] = distance[row][col] + count
                queue.append((nr - dr[i], nc - dc[i]))

    if distance[end[0]][end[1]] < MAX:
        return distance[end[0]][end[1]]
    else:
        return -1



matrix = [[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 0, 0, 0]]

print(maze_II(matrix, (0,4), (4,4)))
