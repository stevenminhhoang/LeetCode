class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.arr = [None] * self.m



    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key % self.m
        if self.arr[index] is None:
            self.arr[index] = ListNode(key, value)
        else:
            curr = self.arr[index]
            while True:
                if curr.pair[0] == key:
                    curr.pair = (key, value)
                    return
                if curr.next is None:
                    break
                curr = curr.next

            curr.next = ListNode(key, value)



    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.m
        curr = self.arr[index]
        while curr:
            if curr.pair[0] == key:
                return curr.pair[1]

            curr = curr.next

        return -1


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.m
        curr = prev = self.arr[index]
        if curr is None:
            return
        if curr.pair[0] == key:
            self.arr[index] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.pair[0] == key:
                    prev.next = curr.next
                    break
                else:
                    prev = curr
                    curr = curr.next





# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
