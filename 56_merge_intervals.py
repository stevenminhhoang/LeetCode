# O(n*log(n))
def merge_intervals(intervals):
    if not intervals:
        return []

    res = []
    intervals.sort(key = lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    for interval in intervals:
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
            res.append([start, end])
            start = interval[0]
            end = interval[1]

    # add last interval
    res.append([start, end])

    return res

# print(merge_intervals([[1,4],[4,5]]))
print(merge_intervals([[1,4],[2,3]]))
# print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
