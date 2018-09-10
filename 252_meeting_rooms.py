# O(n * log(n))
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True

        intervals.sort(key = lambda x: x.start)
        prev = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < prev:
                return False
            prev = intervals[i].end

        return True
