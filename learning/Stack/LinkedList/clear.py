class Node:

    def __init__(self, value):

        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):

        self.top = None
        self.length = 0
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1
            
    def pop(self):
        if self.length == 0:
            return
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.length -= 1
        return temp.value
            
    def peek(self):
     return self.top
 
    def __str__(self):
            current = self.top
            values = []
            while current:
                values.append(str(current.value))
                current = current.next
            return ' -> '.join(values)
        
    def is_empty(self):
        return self.top is None
    
    def clear(self):
        self.top = None
        self.length = 0
            



my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack)