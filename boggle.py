import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.is_word

    def start_with(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True

def boggle(grid, dic):
    def dfs(grid, row, col, visited, string, res):
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            return
        if visited[row][col]:
            return

        string += grid[row][col]
        if not trie.start_with(string):
            return
        if trie.search(string):
            res.add(string)

        visited[row][col] = True
        for (nr, nc) in ((row + 1, col - 1), (row + 1, col), (row + 1, col + 1),
                         (row, col - 1), (row, col + 1),
                         (row - 1, col - 1), (row - 1, col), (row - 1, col + 1)):
            dfs(grid, nr, nc, visited, string, res)

        visited[row][col] = False


    trie = Trie()
    for word in dic:
        trie.insert(word)

    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
    res = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dfs(grid, i, j, visited, "", res)

    return list(res)



dic = {"GEEKS", "FOR", "QUIZ", "GO", "GEE"}
grid = [["G","I","Z"],
        ["U","E","K"],
        ["Q","S","E"]]

print(boggle(grid, dic))
