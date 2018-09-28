# O(n * log(n))
import heapq
def skyline_problem(buildings):
    position = sorted(set(x for b in buildings for x in (b[0],b[1])))
    prevH = 0
    i = 0
    heap, res = [], []
    for curr in position:
        while heap and heap[0][1] <= curr:
            heapq.heappop(heap)
        while i < len(buildings) and buildings[i][0] <= curr:
            heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))
            i += 1

        if heap:
            currH = -heap[0][0]
            if currH != prevH:
                res.append([curr, currH])
                prevH = currH
        # no building, horizon
        else:
            res.append([curr, 0])

    return res


print(skyline_problem([[1,3,3],[2,4,4],[5,8,2],[6,7,4],[8,9,4]]))
