class MinStack(object):
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        self.s.pop()


    def top(self):
        return self.s[-1]


    def getMin(self):
        if len(self.s) == 0:
            return None
        else:
            return 
