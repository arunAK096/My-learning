class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None   


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None    
        self.length = 0     

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1


my_list = LinkedList()


my_list.append(20)

my_list.append(30)

# Print values to verify
print("Head Node Value:", my_list.head.value)
print("Tail Node Value:", my_list.tail.value) 
print("Total List Length:", my_list.length)  