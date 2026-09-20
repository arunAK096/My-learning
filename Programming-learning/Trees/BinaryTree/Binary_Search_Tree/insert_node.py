class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
   
newBT = BinaryTree("20")
leftChild = BinaryTree("15")
rightChild = BinaryTree("30")
newBT.left = leftChild
newBT.right = rightChild     
        
def insertNode(rootNode, nodeValue):
    if rootNode.data:
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
            
print(insertNode(newBT, 50))
        
