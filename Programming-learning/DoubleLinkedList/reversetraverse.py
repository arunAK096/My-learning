class Node:
    def __init__(self, value):

        self.value = value
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += f'{temp_node.value}  '
            if temp_node.next is not None:
                result += '<- -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        
    def prepand(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        self.length += 1
        
    def reverse_traverse(self):
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.prev

        
newdll = Linkedlist()
newdll.append(1)
newdll.append(2)
newdll.append(3)
newdll.prepand(0)
print(newdll)
newdll.reverse_traverse()