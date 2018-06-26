def maxAreaOfIsland(self, grid):
    def get_area(grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return 0

        if grid[row][col] == 0:
            return 0

        grid[row][col] = 0

        return 1 + get_area(grid, row - 1, col) + get_area(grid, row + 1, col) + get_area(grid, row, col - 1) + get_area(grid, row, col + 1)

    max_area = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                size = get_area(grid, row, col)
                max_area = max(size, max_area)

    return max_area
