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
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node

        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

        self.length += 1
        
cslist = CircularSinglyLinkedList(10)
cslist.append(20)
cslist.append(30)   
cslist.append(40)      
print(cslist.head.value)
print(cslist.tail.value)
print(cslist.tail.next.value)
print(cslist.length)