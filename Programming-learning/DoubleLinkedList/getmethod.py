class Node:
    def __init__(self, value):

        self.value = value
        self.next = None
        self.prevs = None

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
        
newdll = Linkedlist()
newdll.append(1)
newdll.append(2)
newdll.append(4)
newdll.append(3)
newdll.prepand(0)
print(newdll)
print(newdll.get(3))