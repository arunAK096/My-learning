class Node:

    def __init__(self, value):

        self.value = value
        self.next = None
        self.previous = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def pop_first(self):
        if self.head is None:
            return None
        pop_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
            pop_node.next = None
        self.length -= 1
        return pop_node