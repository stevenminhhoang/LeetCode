import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.index = -1
        self.palindromes_below = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ans = []

    def insert(self, word, i):
        curr = self.root
        for j in range(len(word) - 1, -1, -1):
            curr = curr.children[word[j]]
            if j > 0 and is_palindrome(word[:j]):
                curr.palindromes_below.append(i)

        curr.index = i

    def check_word(self, word, i):
        curr = self.root
        if curr.index >= 0 and is_palindrome(word) and i != curr.index:
            self.ans.append([i, curr.index])
            self.ans.append([curr.index, i])

        for j in range(len(word)):
            if word[j] not in curr.children:
                return
            curr = curr.children[word[j]]
            if curr.index >= 0 and i != curr.index and is_palindrome(word[j+1:]):
                self.ans.append([i, curr.index])

        for j in curr.palindromes_below:
                if i != j:
                    self.ans.append([i,j])


def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def palindrome_pairs(words):
    trie = Trie()
    for i, word in enumerate(words):
        trie.insert(word, i)
    for i, word in enumerate(words):
        trie.check_word(word, i)

    return trie.ans


print(palindrome_pairs(["abcd","dcba","lls","s","sssll"]))
# print(palindrome_pairs(["bat","tab","cat"]))
