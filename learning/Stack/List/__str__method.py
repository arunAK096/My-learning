class Stack:

    def __init__(self):
        self.items = []
        
    def push(self, element):
        self.items.append(element)
        
    def is_empty(self):
        return len(self.items) == 0
        
    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)
        
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.is_empty())