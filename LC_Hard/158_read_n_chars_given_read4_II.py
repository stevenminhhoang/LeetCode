# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buffPtr = 0
        self.buffCount = 0
        self.temp = [0] * 4
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        total = 0
        while total < n:
            # no remaining characters in the temp
            if self.buffPtr == 0:
                self.buffCount = read4(self.temp)
            if self.buffCount == 0:
                break
            while total < n and self.buffPtr < self.buffCount:
                buf[total] = self.temp[self.buffPtr]
                total += 1
                self.buffPtr += 1

            if self.buffPtr >= self.buffCount:
                self.buffPtr = 0

        return total
