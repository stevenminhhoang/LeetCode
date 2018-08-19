# O(M * N)
import collections
drow = [-1, 0, 1, -1, 1, -1, 0, 1]
dcol = [-1, -1, -1, 0, 0, 1, 1, 1]

def print_matrix(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end = ' ')
        print()

# DFS
# def minesweeper(board, click):
#     def dfs(board, row, col):
#         if not (0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'E'):
#             return
#
#         num = num_of_bombs(board, row, col)
#         if num == 0:
#             board[row][col] = 'B'
#             for i in range(8):
#                 n_row, n_col = row + drow[i], col + dcol[i]
#                 dfs(board, n_row, n_col)
#         else:
#             board[row][col] = str(num)
#
#     def num_of_bombs(board, row, col):
#         num = 0
#         for i in range(8):
#             n_row, n_col = row + drow[i], col + dcol[i]
#             if not (0 <= n_row < len(board) and 0 <= n_col < len(board[0])):
#                 continue
#             if board[n_row][n_col] == 'X' or board[n_row][n_col] == 'M':
#                 num += 1
#
#         return num
#
#     row, col = click[0], click[1]
#     if board[row][col] == 'M':
#         board[row][col] = 'X'
#         return board
#
#     dfs(board, row, col)
#     return board

# BFS
def minesweeper(board, click):
    queue = collections.deque()
    queue.append((click[0], click[1]))
    while queue:
        row, col = queue.popleft()
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            num = 0
            for i in range(8):
                n_row, n_col = row + drow[i], col + dcol[i]
                if not (0 <= n_row < len(board) and 0 <= n_col < len(board[0])):
                    continue
                if board[n_row][n_col] == 'X' or board[n_row][n_col] == 'M':
                    num += 1

            if num > 0:
                board[row][col] = str(num)
            else:
                board[row][col] = 'B'
                for i in range(8):
                    n_row, n_col = row + drow[i], col + dcol[i]
                    if not (0 <= n_row < len(board) and 0 <= n_col < len(board[0])):
                        continue
                    if board[n_row][n_col] == 'E':
                        board[n_row][n_col] = 'B'
                        queue.append((n_row, n_col))

    return board


grid = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

print_matrix(minesweeper(grid, [3, 0]))
