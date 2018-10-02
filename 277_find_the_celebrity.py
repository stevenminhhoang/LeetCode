# O(n)
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0

        stack = []
        for i in range(n):
            stack.append(i)

        a, b = 0, 0
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            if knows(a, b):
                stack.append(b)
            else:
                stack.append(a)

        c = stack.pop()
        for i in range(n):
            if i != c and (knows(c, i) or not knows(i, c)):
                return -1

        return c
