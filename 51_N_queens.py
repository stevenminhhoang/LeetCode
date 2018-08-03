# O(n^n)
def N_queens(n):
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
        for i, j in zip(range(row + 1, n), reversed(range(col))):
            if board[i][j] == 'Q':
                return False

        return True

    def backtrack(lis, col, board):
        if col == n:
            temp = []
            for row in board:
                string = ""
                for char in row:
                    string += char
                temp.append(string)
            lis.append(temp)
            return

        for row in range(n):
            if valid(row, col, board):
                board[row][col] = 'Q'
                backtrack(lis, col + 1, board)
                board[row][col] = '.'

    lis = []
    board = [['.' for j in range(n)] for i in range(n)]
    backtrack(lis, 0, board)
    return lis

print(N_queens(4))

# for i, j in zip(range(3, 4), reversed(range(2))):
#     print(i, j)
