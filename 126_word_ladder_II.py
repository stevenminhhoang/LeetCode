# O(b^d) where b is number of neighbors and d is distance from start to end
import collections, string
def word_ladder_II(start, end, word_list):
    def get_neighbors(word, dic):
        res = []
        for i in range(len(word)):
            part1, part2 = word[:i], word[i + 1:]
            for j in string.ascii_lowercase:
                if j != word[i]:
                    next_word = part1 + j + part2
                    if next_word in dic:
                        res.append(next_word)

        return res


    def bfs(start, end, dic, distance, node_neighbors):
        queue = collections.deque()
        queue.append(start)
        distance[start] = 0
        while queue:
            size = len(queue)
            found = False
            for i in range(size):
                curr = queue.popleft()
                curr_distance = distance[curr]
                neighbors = get_neighbors(curr, dic)
                for nei in neighbors:
                    node_neighbors[curr].append(nei)
                    if nei not in distance:
                        distance[nei] = curr_distance + 1
                        if end == nei:
                            found = True
                        else:
                            queue.append(nei)

                if found:
                    break

    def dfs(curr, end, dic, distance, node_neighbors, temp, res):
        temp.append(curr)
        if end == curr:
            res.append(temp[:])
        else:
            for nei in node_neighbors[curr]:
                if distance[nei] == distance[curr] + 1:
                    dfs(nei, end, dic, distance, node_neighbors, temp, res)

        temp.pop()


    res = []
    dic = set(word_list)
    dic.add(start)
    distance = collections.Counter()
    node_neighbors = collections.defaultdict(list)
    if end not in word_list:
        return []

    bfs(start, end, dic, distance, node_neighbors)
    dfs(start, end, dic, distance, node_neighbors, [], res)
    return res


print(word_ladder_II("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
