# O(mn * 4^k) k is length of word
def word_search(grid, word):
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


grid = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(word_search(grid, "ABCCEDFS"))
