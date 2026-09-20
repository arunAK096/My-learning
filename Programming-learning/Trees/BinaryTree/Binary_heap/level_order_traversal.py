class Heap:
    def __init__(self, size):
        self.customlist = (size+1) * [None]
        self.heapsize = 0
        self.maxsize = size + 1

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapsize + 1):
            print(rootNode.customlist[i])
            
newbinaryHeap = Heap(5)
print(newbinaryHeap.customlist)