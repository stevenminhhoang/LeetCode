class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.pos = {}


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.arr.append(val)
            self.pos[val] = len(self.arr) - 1
            return True

        return False


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            index = self.pos[val]
            last = self.arr[-1]
            self.arr[index] = last
            self.pos[last] = index
            self.arr.pop()
            self.pos.pop(val, 0)
            return True

        return False



    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.arr[random.randrange(0, len(self.arr))]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
