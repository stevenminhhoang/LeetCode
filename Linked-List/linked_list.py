class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            cur = next
        self.head = prev

    def get_mid(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

    def print_reverse(self):
        nodes = []
        head = self.head
        while head:
            nodes.append(head.val)
            head = head.next
        while nodes:
            print(nodes.pop())




A = LinkedList()
A.push(1)
A.push(2)
A.push(3)

A.print_list()
