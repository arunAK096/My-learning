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


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack)