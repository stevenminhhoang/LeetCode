# O(n * log(26)) ~ O(n)
import collections, heapq
def task_scheduler(tasks, n):
    count = collections.Counter(tasks)
    heap = [-val for val in count.values()]
    heapq.heapify(heap)
    ans = 0
    while heap:
        interval = n + 1
        temp = []
        while interval > 0 and heap:
            count = heapq.heappop(heap)
            count += 1
            temp.append(count)
            interval -= 1
            ans += 1

        for item in temp:
            if item < 0:
                heapq.heappush(heap, item)

        if not heap:
            break

        # if interval > 0, the machine will become idle
        ans += interval

    return ans

print(task_scheduler(["A","A","A","B","B","B"], 2))
