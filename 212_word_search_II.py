# O(row * col * 4^m * m) m is length of word
from Trie import Trie
def word_search_II(board, words):
    def dfs(board, visited, res, string, i, j, trie):
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return
        if visited[i][j]:
            return

        string += board[i][j]
        if not trie.startsWith(string):
            return
        if trie.search(string):
            res.add(string)

        visited[i][j] = True
        dfs(board, visited, res, string, i - 1, j, trie)
        dfs(board, visited, res, string, i + 1, j, trie)
        dfs(board, visited, res, string, i, j - 1, trie)
        dfs(board, visited, res, string, i, j + 1, trie)
        # Backtrack
        visited[i][j] = False


    res = set()
    visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
    trie = Trie()
    for word in words:
        trie.insert(word)
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, visited, res, "", i, j, trie)

    return list(res)


board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
print(word_search_II(board, words))
