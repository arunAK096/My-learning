class Node:

    def __init__(self, value):

        self.value = value
        self.next = None
        self.previous = None
        
    def __str__(self):
        return str(self.value)
        
class CircularDoublyLinkedList:
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
    
newdll = CircularDoublyLinkedList()



