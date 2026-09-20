class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CircularSinglyLinkedList:

    def __init__(self, value):

        newNode = Node(value)

        newNode.next = newNode

        self.head = newNode

        self.tail = newNode

        self.length = 1
        
cslist = CircularSinglyLinkedList(10)
print(cslist.head.value)
print(cslist.tail.value)