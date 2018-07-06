def solve_maze(maze):
    def print_sol(sol):
        for i in range(len(sol)):
            for j in range(len(sol[0])):
                print(sol[i][j], end="")
            print("")

    def is_valid(maze, x, y):
        if not (0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1):
            return False
        return True

    def solve_maze_util(maze, x, y, sol):
        if x == len(sol) - 1 and y == len(sol[0]) - 1:
            sol[x][y] = 1
            return True

        if is_valid(maze, x, y):
            sol[x][y] = 1

            if solve_maze_util(maze, x + 1, y, sol):
                return True
            if solve_maze_util(maze, x, y + 1, sol):
                return True

            sol[x][y] = 0
            return False

    sol = [[0 for col in range(len(maze))] for row in range(len(maze[0]))]
    if not solve_maze_util(maze, 0, 0, sol):
        return False

    print_sol(sol)
    return True

maze = [ [1, 1, 0, 1],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]

solve_maze(maze)
