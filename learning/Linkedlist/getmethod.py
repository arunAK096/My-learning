class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None   


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None    
        self.length = 0     
        
    def __str__(self):
        tempnode = self.head
        result = ""
        while tempnode is not None:
            result += str(tempnode.value)
            if tempnode.next is not None:
                result += " -> "
            tempnode = tempnode.next
        return result

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
                 
    
    def get(self, index):
        if index < -1 or index >= self.length:
            return None
        if index == -1:
            return self.tail.value
        current = self.head
        for _ in range(index):
            current = current.next
        return current



my_list = LinkedList()


my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.append(60)
print(my_list)
print(my_list.get(3)) 