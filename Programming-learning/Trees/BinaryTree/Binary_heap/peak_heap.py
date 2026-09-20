class Heap:
    def __init__(self, size):
        self.customlist = (size+1) * [None]
        self.heapsize = 0
        self.maxsize = size + 1
        
        
def peakHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customlist[1]
        
def sizeHeap(rootNode):
    if not rootNode:
         return
    else:
        return rootNode.heapsize 
            
newbinaryHeap = Heap(5)
print(newbinaryHeap.customlist)