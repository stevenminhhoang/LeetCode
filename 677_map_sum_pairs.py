# O(k) insert where k is length of key. O(k) sum as well
import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.count = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key, val):
        current = self.root
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        current.count += delta
        for char in key:
            current = current.children[char]
            current.count += delta

    def sum(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]

        return current.count
