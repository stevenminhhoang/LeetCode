# O(m * n)
import collections
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def maze(maze, start, destination):
    visited = set()
    visited.add((start[0], start[1]))
    queue = collections.deque()
    queue.append((start[0], start[1]))
    while queue:
        row, col = queue.popleft()
        if row == destination[0] and col == destination[1]:
            return True
        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]
            while (0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] == 0):
                nr += dr[i]
                nc += dc[i]
            if (nr - dr[i], nc - dc[i]) not in visited:
                queue.append((nr - dr[i], nc - dc[i]))
                visited.add((nr - dr[i], nc - dc[i]))

    return False


grid = [[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 0, 0, 0]]

print(maze(grid, [0, 4], [4, 4]))
