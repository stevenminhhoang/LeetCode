# O(m * n)
dr = [1,0,-1,0]
dc = [0,1,0,-1]
import collections
def print_matrix(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=' ')
        print()

def surrounding_regions(board):
    if not board:
        return
    queue = collections.deque()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if ((i in (0, len(board) - 1)) or (j in (0, len(board[0]) - 1))) and board[i][j] == "O":
                queue.append((i, j))
                board[i][j] = "*"

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == "O"):
                continue
            board[nr][nc] = "*"
            queue.append((nr, nc))


    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "*":
                board[row][col] = "O"
            else:
                board[row][col] = "X"

    return board


board = [["X", "X", "X", "X"],
["X", "O", "O", "X"],
["X", "X", "O", "X"],
["X", "O", "X", "X"]]

print_matrix(surrounding_regions(board))
