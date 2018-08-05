import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

def create_trie(words):
    root = TrieNode()
    for word in words:
        curr = root
        for char in word:
            curr = curr.children[char]
        curr.is_word = True

    return root

def search_prefix(root, prefix):
    curr = root
    for i, char in enumerate(prefix):
        if curr.is_word:
            return prefix[:i]
        if char not in curr.children:
            break
        curr = curr.children[char]

    return prefix

def replace_words(dic, sentence):
    root = create_trie(dic)
    res = []
    for word in sentence.split():
        res.append(search_prefix(root, word))

    return " ".join(res)


print(replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
