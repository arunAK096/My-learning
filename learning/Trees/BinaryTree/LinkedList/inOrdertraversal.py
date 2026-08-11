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

def inOrdertraversal(rootNode):
    if not rootNode:
        return
    inOrdertraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrdertraversal(rootNode.rightChild)

inOrdertraversal(newBT)


