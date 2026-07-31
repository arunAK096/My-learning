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
        
newdll = Linkedlist()
newdll.append(1)
newdll.append(2)
newdll.append(3)
print(newdll)

        
