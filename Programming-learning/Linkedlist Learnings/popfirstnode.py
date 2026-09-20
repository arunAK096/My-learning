class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def pop_first(self):
        if self.length == 0:
            return None
        
        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            popped_node.next = None

        self.length -= 1

        return popped_node