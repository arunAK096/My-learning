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
newBT.rightChild.leftChild = leftChild

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

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully inserted"
            
def getDeepestNode(rootNode):
    if not rootNode:
            return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if(root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode
    
def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild is dNode:
                root.value.rightChild = None
                return
            else:
                customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild is dNode:
                root.value.leftChild = None
                return
            else:
                customQueue.enqueue(root.value.leftChild)
                
def deleteNodeBt(rootNode, node):
    if not rootNode:
        return "The BT does not exist"
    else:   
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.date == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            else:
                root = customQueue.dequeue()
                if root.value.leftChild is not None:
                    customQueue.enqueue(root.value.leftChild)
                if root.value.rightChild is not None:
                    customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"
    
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted"

deleteBT(newBT)
levelOrderTraversal(newBT)