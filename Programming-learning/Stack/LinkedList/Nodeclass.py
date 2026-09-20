class Node:

    def __init__(self, value):

        self.value = value
        self.next = None
        
class Stack:
     def __init__(self):

        self.top = None
        self.length = 0
        
# single element version
# class Stack:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.top = new_node
#         #self.length = 1

my_stack = Stack()
print(my_stack)