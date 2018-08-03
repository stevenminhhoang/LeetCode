def total_N_queens(n):
    def valid(row, col, board):
        # Check row on the left side of Q
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        # Check upper diagonal on left side of Q
        for i,j in zip(reversed(range(row)), reversed(range(col))):
            if board[i][j] == 'Q':
                return False
        # Check lower diagonal on left side of Q
        for i,j in zip(range(row + 1, n), reversed(range(col))):
            if board[i][j] == 'Q':
                return False

        return True

    def backtrack(lis, col, board):
        global count
        if col == len(board):
            temp = []
            for row in board:
                string = ""
                for char in row:
                    string += char
                temp.append(string)

            lis.append(temp)
            count += 1
            return

        for row in range(n):
            if valid(row, col, board):
                board[row][col] = 'Q'
                backtrack(lis, col + 1, board)
                board[row][col] = '.'

    global count
    lis, count = [], 0
    board = [['.' for j in range(n)] for i in range(n)]
    backtrack(lis, 0, board)
    return count


print(total_N_queens(4))
