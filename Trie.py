# O(n)
import collections

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            current = current.children[char]
        current.is_word = True

    # def search(self, word):
    #     current = self.root
    #     for char in word:
    #         if char not in current.children:
    #             return False
    #         current = current.children[char]
    #
    #     return current.is_word

    # DFS
    def search(self, word):
        def dfs(curr, word):
            if len(word) == 0:
                return curr.is_word

            first = word[0]
            if first not in curr.children:
                return False

            return dfs(curr.children[first], word[1:])

        return dfs(self.root, word)



    def startsWith(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
# print(trie.search("app"))
# print(trie.startsWith("app"))
# trie.insert("app")
# print(trie.search("app"))
