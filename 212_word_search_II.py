def word_search_II(board, words):
    def exist(grid, word):
        def dfs(grid, i, j, start, word, visited):
            if start == len(word):
                return True
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return False
            if visited[i][j] or word[start] != grid[i][j]:
                return False

            visited[i][j] = True
            if (dfs(grid, i - 1, j, start + 1, word, visited)
                or dfs(grid, i + 1, j, start + 1, word, visited)
                or dfs(grid, i, j - 1, start + 1, word, visited)
                or dfs(grid, i, j + 1, start + 1, word, visited)):
                return True

            visited[i][j] = False
            return False

        visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(grid, i, j, 0, word, visited):
                    return True

        return False


    ans = []
    for word in words:
        if exist(board, word):
            ans.append(word)

    return ans

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain","ath","hklfhi"]
print(word_search_II(board, words))
