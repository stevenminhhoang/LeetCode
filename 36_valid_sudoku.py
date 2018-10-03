# O(1)
def valid_sudoku(board):
    def valid(board, row, col):
        temp = board[row][col]
        board[row][col] = '*'
        for i in range(9):
            if board[i][col] == temp:
                return False
        for i in range(9):
            if board[row][i] == temp:
                return False
        for i in range(3):
            for j in range(3):
                if board[(row // 3) * 3 + i][(col // 3) * 3 + j] == temp:
                    return False
        
        board[row][col] = temp
        return True

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '.':
                continue
            if not valid(board, row, col):
                return False

    return True
