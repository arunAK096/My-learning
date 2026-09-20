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
                currentNode = currentNode.previous
        return currentNode
    
    def pop_first(self):
            if self.length == 0:
                return None
            pop_node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                pop_node.prev = None
                pop_node.next = None
                self.head.prev = self.tail
                self.tail.next = self.head
            self.length -= 1
            return pop_node
    
    def pop(self):
        if self.length == 0:
            return None
        pop_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            pop_node.next = None
            pop_node.previous = None
            self.tail.next = self.head
            self.head.previous = self.tail
        self.length -= 1
        return pop_node
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pop_node = self.get(index)
        pop_node.previous.next = pop_node.next
        pop_node.next.previous = pop_node.previous
        pop_node.next = None
        pop_node.previous = None
        self.length -= 1
        return pop_node
    
newdll = CircularDoublyLinkedList()
newdll.append(1)
newdll.append(2)
newdll.append(3)
newdll.append(3)
print(newdll)
newdll.prepend(0)
print(newdll)


