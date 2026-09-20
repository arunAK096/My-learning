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
            
def heapifyTreeInsert(rootNode, index, heaptype):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heaptype == "Min":
        if rootNode.customlist[index] < rootNode.customlist[parentIndex]:
            temp = rootNode.customlist[index]
            rootNode.customlist[index] = rootNode.customlist[parentIndex]
            rootNode.customlist[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heaptype)
    elif heaptype == "Max":
        if rootNode.customlist[index] > rootNode.customlist[parentIndex]:
            temp = rootNode.customlist[index]
            rootNode.customlist[index] = rootNode.customlist[parentIndex]
            rootNode.customlist[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heaptype)
        
def insertNode(rootNode, nodeValue, heaptype):
    if rootNode.heapsize + 1 == rootNode.maxsize:
        return "The Binary Heap is Full"
    rootNode.customlist[rootNode.heapsize + 1] = nodeValue
    rootNode.heapsize += 1
    heapifyTreeInsert(rootNode, rootNode.heapsize, heaptype)
    return "The value has been successfully inserted"



newbinaryHeap = Heap(5)
print(newbinaryHeap.customlist)