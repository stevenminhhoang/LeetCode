class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.grid = [['_' for j in range(n)] for i in range(n)]
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.grid[row][col] = player
        for i in range(1, self.n):
            if self.grid[row][i] != self.grid[row][i - 1]:
                break
            if i == self.n - 1:
                return player

        for i in range(1, self.n):
            if self.grid[i][col] != self.grid[i - 1][col]:
                break
            if i == self.n - 1:
                return player

        if row == col:
            for i in range(1, self.n):
                if self.grid[i][i] != self.grid[i - 1][i - 1]:
                    break
                if i == self.n - 1:
                    return player

        if row + col == self.n - 1:
            for i in range(1, self.n):
                if self.grid[self.n - 1 - i][i] != self.grid[self.n - i][i - 1]:
                    break
                if i == self.n - 1:
                    return player

        return 0





# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
