# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        temp = [0] * 4
        total = 0
        while total < n:
            count = read4(temp)
            count = min(count, n - total)
            if count == 0:
                break
            for i in range(count):
                buf[total] = temp[i]
                total += 1

        return total
            
