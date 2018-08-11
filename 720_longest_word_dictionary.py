# O(∑w_i), where w_i is the length of words[i].
import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
        self.word = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_word = True
        curr.word = word

    def bfs(self):
        queue = collections.deque([self.root])
        res = ''
        while queue:
            curr = queue.popleft()
            for node in curr.children.values():
                if node.is_word:
                    queue.append(node)
                    if len(node.word) > len(res) or node.word < res:
                        res = node.word

        return res

def longest_word_dictionary(words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    return trie.bfs()


# print(longest_word_dictionary(["w","wo","wor","worl", "world"]))
print(longest_word_dictionary(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
