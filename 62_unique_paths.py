# Memoization
def valid_square(grid, row, col):
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        return False
    return True

def is_at_end(grid, row, col):
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return True
    return False


def count_paths_util(grid, row, col, paths):
    if not valid_square(grid, row, col):
        return 0
    if is_at_end(grid, row, col):
        return 1

    if paths[row][col] == 0:
        paths[row][col] = count_paths_util(grid, row + 1, col, paths) + count_paths_util(grid, row, col + 1, paths)

    return paths[row][col]


def count_paths(row, col):
    grid = [[0 for i in range(col)] for j in range(row)]
    paths = [[0 for i in range(col)] for j in range(row)]
    return count_paths_util(grid, 0, 0, paths)

print(count_paths(3, 7))

# DP
def unique_path(row, col):
    path = [[0 for j in range(col)] for i in range(row)]
    for i in range(row):
        path[i][0] = 1
    for j in range(col):
        path[0][j] = 1

    for r in range(1, row):
        for c in range(1, col):
            path[r][c] = path[r - 1][c] + path[r][c - 1]

    return path[-1][-1]

print(unique_path(3, 7))
