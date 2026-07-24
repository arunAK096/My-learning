class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
new_linked_list = LinkedList()
print(new_linked_list.head)
print(new_linked_list.tail)
print(new_linked_list.length)