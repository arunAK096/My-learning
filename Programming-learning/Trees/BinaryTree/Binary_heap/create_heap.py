class Heap:
    def __init__(self, size):
        self.customlist = (size+1) * [None]
        self.heapsize = 0
        self.maxsize = size + 1
        
        
newbinaryHeap = Heap(5)
print(newbinaryHeap.customlist)