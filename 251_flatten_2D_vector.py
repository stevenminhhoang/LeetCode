class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.queue = collections.deque()
        for row in vec2d:
            for x in row:
                self.queue.append(x)



    def next(self):
        """
        :rtype: int
        """
        if self.hasNext:
            return self.queue.popleft()


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
