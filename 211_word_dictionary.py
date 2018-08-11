import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word):
        return self.dfs(self.root, word)

    def dfs(self, curr, word):
        if len(word) == 0:
            return curr.is_word

        first = word[0]
        if first == '.':
            for node in curr.children:
                if self.dfs(curr.children[node], word[1:]):
                    return True
        else:
            if first not in curr.children:
                return False

            return self.dfs(curr.children[first], word[1:])

        return False


trie = WordDictionary()
trie.addWord("bad")
trie.addWord("dad")
trie.addWord("map")
print(trie.search("..."))
