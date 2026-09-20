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
        
    def prepand(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node

        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.length += 1        
        
    def __str__(self):
        temp = self.head
        result = ""
        while temp is not None:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += " -> "
        return result
    
    def pop_first(self):
        if self.length == 0:
            return None
        pop_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            pop_node.next = None
        self.length -= 1
        return pop_node
    
cslist = CircularSinglyLinkedList(10)
cslist.append(20)
cslist.append(30)   
cslist.append(40)      
print(cslist)
cslist.prepand(5)
print(cslist)
