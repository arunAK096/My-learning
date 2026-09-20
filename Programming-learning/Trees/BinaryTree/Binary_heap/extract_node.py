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
            
def heapifyextract(rootNode, index, heaptype):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapsize < leftIndex:
        return
    elif rootNode.heapsize == leftIndex:
        if heaptype == "Min":
            if rootNode.customlist[index] > rootNode.customlist[leftIndex]:
                temp = rootNode.customlist[index]
                rootNode.customlist[index] = rootNode.customlist[leftIndex]
                rootNode.customlist[leftIndex] = temp
            return
        else:
            if rootNode.customlist[index] < rootNode.customlist[leftIndex]:
                temp = rootNode.customlist[index]
                rootNode.customlist[index] = rootNode.customlist[leftIndex]
                rootNode.customlist[leftIndex] = temp
            return
    else:
        if heaptype == "Max":
            if rootNode.customlist[leftIndex] < rootNode.customlist[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customlist[index] > rootNode.customlist[swapChild]:
                temp = rootNode.customlist[index]
                rootNode.customlist[index] = rootNode.customlist[swapChild]
                rootNode.customlist[swapChild] = temp
        else:
            if rootNode.customlist[leftIndex] > rootNode.customlist[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customlist[index] < rootNode.customlist[swapChild]:
                temp = rootNode.customlist
                rootNode.customlist[index] = rootNode.customlist[swapChild]
                rootNode.customlist[swapChild] = temp
    heapifyextract(rootNode, swapChild, heaptype)
    
def extractNode(rootNode, heaptype):
    if rootNode.heapsize == 0:
        return
    else:
        extractedNode = rootNode.customlist[1]
        rootNode.customlist[1] = rootNode.customlist[rootNode.heapsize]
        rootNode.customlist[rootNode.heapsize] = None
        rootNode.heapsize -= 1
        heapifyextract(rootNode, 1, heaptype)
        return extractedNode
                


newbinaryHeap = Heap(5)
print(newbinaryHeap.customlist) 