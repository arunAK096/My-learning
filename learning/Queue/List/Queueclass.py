class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        return self.items == []
    
    
    def size(self):
        return len(self.items)
        
    def Enqueue(self, element):
        self.items.append(element)
        
    def Dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = []

        
my_queue = Queue()
my_queue.Enqueue(1)
my_queue.Enqueue(2)
my_queue.Enqueue(3)
my_queue.delete()
print(my_queue)