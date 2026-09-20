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

    def get(self, index):

        if index < 0 or index >= self.length:
            return None
        currentNode = None
        if index < self.length // 2:
            currentNode = self.head
            for _ in range(index):
                currentNode = currentNode.next
        else:
            currentNode = self.tail
            for _ in range(self.length - 1, index, -1):
                currentNode = currentNode.prev
        return currentNode
    
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        
newdll = CircularDoublyLinkedList()
newdll.append(1)
newdll.append(2)
newdll.append(3)
newdll.append(3)
print(newdll)
newdll.prepend(0)
print(newdll)
newdll.set(4,4)
print(newdll)

