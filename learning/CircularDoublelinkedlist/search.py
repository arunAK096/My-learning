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
        
    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current.value)
            current = current.next
            if current == self.head:
                break
            result += " ⇄ "
        return result
        

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
        
    def prepend(self, value):
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
            self.head = newNode
        self.length += 1

    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return True, index
            current = current.next
            index +=1
            if current == self.head:
                break
        return False
        
newdll = CircularDoublyLinkedList()
newdll.append(1)
newdll.append(2)
newdll.append(3)
print(newdll)
newdll.prepend(0)
print(newdll)
print(newdll.search(3))

