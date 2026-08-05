class Stack:

    def __init__(self):
        self.items = []
        
    def push(self, element):
        self.items.append(element)
        
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.items)