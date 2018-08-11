# O(n * log(n))
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: x.start)
        heap = []
        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)

            heapq.heappush(heap, interval.end)

        return len(heap)
