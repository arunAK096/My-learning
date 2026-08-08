class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = None
        
    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ',' + str(self.next)
        return string
    
class stack:
    def __init__(self):
        self.top = None
        self.minimum = None 
        
    def minNode(self):
        if not self.minimum:
            return None
        return self.minimum.value
    
    def push(self, item):
        if self.minimum and (self.minimum.value < item):
            self.minimum = Node(value = self.minimum.value, next =self.minimum.value)
        else:
            self.minimum = Node(value =item, next = self.minimum )
        self.top = Node(value =item, next = self.top)
        
    def pop(self):
        if not self.top:
            return None
        self.minimum = self.minimum.next
        item = self.top.value
        self.top = self.top.next
        return item
    
customstack = stack()
customstack.push(10)
customstack.push(20)
customstack.push(30)
print(customstack.minNode())
print(customstack.pop())
print(customstack.minNode())
print(customstack.pop())
print(customstack.minNode()) 