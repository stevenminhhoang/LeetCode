# O(n^2 * m) where n is the number of entries originally in the dictionary and m is the size of the string
import collections, string
def word_ladder(start, end, wordList):
    ls = string.ascii_lowercase
    word_dict = set(wordList)
    queue = collections.deque()
    queue.append((start, 1))
    visited = set()
    while queue:
        word, distance = queue.popleft()
        if word == end:
            return distance
        for i in range(len(word)):
            part1, part2 = word[:i], word[i + 1:]
            for j in ls:
                if word[i] != j:
                    next_word = part1 + j + part2
                    if next_word not in visited and next_word in word_dict:
                        queue.append((next_word, distance + 1))
                        visited.add(next_word)

    return 0


print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
