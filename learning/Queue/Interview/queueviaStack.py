class Stack:
    def __init__(self):
        self.items = []
        
    def __len__(self):
        return len(self.items)
    
    def push(self, items):
        self.items.append(items)
        
    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

class Queueviastack:
    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()
        
    def enqueue(self, items):
        self.instack.push(items)
        
    def dequeue(self):
        while len(self.instack):
            self.outstack.push(self.instack.pop())
        result = self.outstack.pop()
        while len(self.outstack):
            self.instack.push(self.outstack.pop())
        return result
    
custom = Queueviastack()
custom.enqueue(1)
custom.enqueue(2)
custom.enqueue(3)
custom.enqueue(4)
print(custom.dequeue())
print(custom.dequeue())
