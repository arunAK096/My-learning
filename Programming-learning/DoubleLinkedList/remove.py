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
    
    def pop(self):
        if self.length == 0:
            return None
        pop_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            pop_node.previous = None
        self.length -= 1
        return pop_node
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
        return current
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pop_node = self.get(index)
        pop_node.previous.next = pop_node.next
        pop_node.next.previous = pop_node.previous
        pop_node.next = None
        pop_node.previous = None
        self.length -= 1
        return pop_node