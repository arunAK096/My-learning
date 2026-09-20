class Node:

    def __init__(self, value):

        self.value = value
        self.next = None
        self.previous = None
        
    def __str__(self):
        return str(self.value)
        
class CircularDoublyLinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.tail.next = self.head
        self.head.previous = self.tail
        self.length = 1

    
newdll = CircularDoublyLinkedList(1)
print(newdll.head)