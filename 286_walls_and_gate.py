# O(M * N)
import collections
drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]
EMPTY = 2147483647
GATE = 0

def print_matrix(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end = ' ')
        print()

def walls_and_gates(rooms):
    queue = collections.deque()
    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] == GATE:
                queue.append((row, col))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            n_row, n_col = r + drow[i], c + dcol[i]
            if not (0 <= n_row < len(rooms) and 0 <= n_col < len(rooms[0]) and rooms[n_row][n_col] == EMPTY):
                continue

            rooms[n_row][n_col] = rooms[r][c] + 1
            queue.append((n_row, n_col))

    return rooms


rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

print_matrix(walls_and_gates(rooms))
