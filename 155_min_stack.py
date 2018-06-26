import collections
class MinStack(object):
    element_with_cache_min = collections.namedtuple('element_with_cache_min', ('element', 'min'))

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._element_with_cache_min = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._element_with_cache_min.append(self.element_with_cache_min(x, x if len(self._element_with_cache_min) == 0 else min(x, self.getMin())))

    def pop(self):
        """
        :rtype: void
        """
        return self._element_with_cache_min.pop().element

    def top(self):
        """
        :rtype: int
        """
        return self._element_with_cache_min[-1].element

    def getMin(self):
        """
        :rtype: int
        """
        return self._element_with_cache_min[-1].min



A = MinStack()
A.push(-2)
A.push(0)
A.push(-3)
print(A.getMin())
A.pop()
print(A.top())
print(A.getMin())
