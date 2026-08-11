from Queue.LinkedList.node_class import Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
leftChild = TreeNode("Tea")
rightChild = TreeNode("Coffee")
newBT.leftChild.leftChild = leftChild
newBT.leftChild.rightChild = rightChild
leftChild = TreeNode("cola")
rightChild = TreeNode("fanta")
newBT.rightChild.leftChild = leftChild
newBT.rightChild.rightChild = rightChild

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if(root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

def searchBT(rootNode, nodeValue):
        if not rootNode:
            return "The BT does not exist"
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not(customQueue.isEmpty()):
                root = customQueue.dequeue()
                if root.value.data == nodeValue:
                    return "Success"
                if(root.value.leftChild is not None):
                    customQueue.enqueue(root.value.leftChild)
                if(root.value.rightChild is not None):
                    customQueue.enqueue(root.value.rightChild)
            return "Not found"

print(searchBT(newBT, "cola"))