class Node:

    def __init__(self, value):

        self.value = value
        self.next = None
        self.previous = None
        
    def __str__(self):
        return str(self.value)
        
class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.previous = newNode
        else:
            self.tail.next = newNode
            self.head.previous = newNode
            newNode.previous = self.tail
            newNode.next = self.head
            self.tail = newNode
        self.length += 1
        

newdll = CircularDoublyLinkedList()
newdll.append(1)
newdll.append(2)
newdll.append(3)
print(newdll.head.previous)