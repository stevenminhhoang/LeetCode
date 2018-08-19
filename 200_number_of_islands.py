import collections
def numIslands(grid):
    def dfs(grid, row, col):
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            return
        if grid[row][col] == 0:
            return
        grid[row][col] = 0

        dfs(grid, row - 1, col)
        dfs(grid, row + 1, col)
        dfs(grid, row, col - 1)
        dfs(grid, row, col + 1)


    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                count += 1
                dfs(grid, row, col)

    return count

print(numIslands([[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]))

# BFS
def bfs(grid, row, col):
    queue = collections.deque([(row, col)])
    while queue:
        r, c = queue.popleft()
        if r > 0 and grid[r- 1][c] == '1':
            queue.append((r - 1, c))
            grid[r - 1][c] = '0'
        if r < len(grid) - 1 and grid[r + 1][c] == '1':
            queue.append((r + 1, c))
            grid[r + 1][c] = '0'
        if c > 0 and grid[r][c - 1] == '1':
            queue.append((r, c - 1))
            grid[r][c - 1] = '0'
        if c < len(grid[0]) - 1 and grid[r][c + 1] == '1':
            queue.append((r, c + 1))
            grid[r][c + 1] = '0'

    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                count += 1
                bfs(grid, r, c)

    return count
