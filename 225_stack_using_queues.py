import collections
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = collections.deque()
        self.q2 = collections.deque()
        self.topStack = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.append(x)
        self.topStack = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        pop_element = self.q1.popleft()

        while self.q2:
            e = self.q2.popleft()
            self.q1.append(e)
            self.topStack = e

        return pop_element

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.topStack

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
