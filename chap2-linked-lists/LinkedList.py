from random import randint

# Linked List Implementation in python

# Node definition
class LinkedListNode:
    def __init__(self, data):
        self.data= data 
        self.next = None 
        self.prev = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        s = "["
        p = self.head
        if p != None :      
            while p.next != None :
                s += str(p.data) + ', '
                p = p.next
            s += str(p.data) + "]"
        return s

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def add(self,data):
        if self.head is None:  # empty list case
            self.tail = self.head = LinkedListNode(data)
        else:
            self.tail.next = LinkedListNode(data)
            self.tail = self.tail.next

    # generate linked list with values between min and max
    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self
