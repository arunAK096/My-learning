class Multistack:
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.customstacks = [0] * (self.numberstacks * stacksize)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize 
        
    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False
        
    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False
        
    def indexofTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1
    
    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return "The stack is full"
        else:
            self.sizes[stacknum] += 1
            self.customstacks[self.indexofTop(stacknum)] = item
            
    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.customstacks[self.indexofTop(stacknum)]
            self.customstacks[self.indexofTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value
        
    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.customstacks[self.indexofTop(stacknum)]
            return value