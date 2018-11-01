def count_battleships(board):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '.':
                continue
            if row > 0 and board[row - 1][col] == 'X':
                continue
            if col > 0 and board[row][col - 1] == 'X':
                continue

            count += 1

    return count

board = [["X",".",".","X"],
        [".",".",".","X"],
        ["X","X",".","X"]]

print(count_battleships(board))
