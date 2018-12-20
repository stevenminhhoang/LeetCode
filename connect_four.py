board = [["." for j in range(6)] for i in range(6)]

def dropPiece(col, player):
    if board[0][col] != ".":
        return

    i = -1
    while board[i][col] != ".":
        i -= 1

    board[i][col] = player
    win = checkForWin(player)
    if win:
        print("Color win: ", win)

def checkForWin(player):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == player:
                i = row
                j = col
                countRow, countCol = 0, 0
                countDiag, countAntiDiag = 0, 0
                while j < 6 and board[row][j] == player:
                    countRow += 1
                    j += 1

                j = col

                while i < 6 and board[i][col] == player:
                    countCol += 1
                    i += 1

                i = row

                while i < 6 and j < 6 and board[i][j] == player:
                    countDiag += 1
                    i += 1
                    j += 1
                i = row
                j = col
                while i >= 0 and j < 6 and board[i][j] == player:
                    countAntiDiag += 1
                    i -= 1
                    j += 1

                if countRow == 4 or countCol == 4 or countDiag == 4 or countAntiDiag == 4:
                    return player


dropPiece(0, "R")
dropPiece(0, "R")
dropPiece(0, "R")
# dropPiece(0, "R")
# dropPiece(3, "R")
# dropPiece(2, "R")
# dropPiece(1, "R")

for row in board:
    print(row)
