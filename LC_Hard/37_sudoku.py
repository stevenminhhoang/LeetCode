# O(9^m) m is the number of empty cells
def sudoku(board):
    def valid(i, j, board):
        temp = board[i][j]
        board[i][j] = '.'
        for row in range(9):
            if board[row][j] == temp:
                return False
        for col in range(9):
            if board[i][col] == temp:
                return False
        for row in range(3):
            for col in range(3):
                if board[(i // 3) * 3 + row][(j // 3) * 3 + col] == temp:
                    return False

        board[i][j] = temp
        return True

    def dfs(board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    for char in '123456789':
                        board[row][col] = char
                        if valid(row, col, board) and dfs(board):
                            return True
                        else:
                            board[row][col] = '.'
                    return False

        return True

    return dfs(board)



print(sudoku(
[["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
))
