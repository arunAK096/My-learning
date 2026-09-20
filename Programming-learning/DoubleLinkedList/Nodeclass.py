class Node:

    def __init__(self, value):

        self.value = value
        self.next = None
        self.previous = None
        
    def __str__(self):
        return f'{self.previous} <- {self.value} -> {self.next}'

new_node = Node(10)
print(new_node)

