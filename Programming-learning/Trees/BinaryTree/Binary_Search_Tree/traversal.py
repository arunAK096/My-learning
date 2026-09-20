from Queue.LinkedList.node_class import Queue


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
   
newBT = BinaryTree(20)
leftChild = BinaryTree(15)
rightChild = BinaryTree(30)
newBT.left = leftChild
newBT.right = rightChild     
        
def insertNode(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.left is None:
            rootNode.left = BinaryTree(nodeValue)
        else:
            insertNode(rootNode.left, nodeValue)
    else:
        if rootNode.right is None:
            rootNode.right = BinaryTree(nodeValue)
        else:
            insertNode(rootNode.right, nodeValue)
    return "The node has been successfully inserted"
            
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)    
    preOrderTraversal(rootNode.right)
    
def InOrderTraversal(rootNode):
    if not rootNode:
        return
    InOrderTraversal(rootNode.left)
    print(rootNode.data)
    InOrderTraversal(rootNode.right)
    
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)  
    print(rootNode.data)
    
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if(root.value.left is not None):
                customQueue.enqueue(root.value.left)
            if(root.value.right is not None):
                customQueue.enqueue(root.value.right)
   
    
    
insertNode(newBT, 13)
insertNode(newBT, 23)
postOrderTraversal(newBT)