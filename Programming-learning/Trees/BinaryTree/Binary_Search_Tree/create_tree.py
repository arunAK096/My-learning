class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
newBT = BinaryTree("Drinks")
leftChild = BinaryTree("Hot")
rightChild = BinaryTree("Cold")
newBT.left = leftChild
newBT.right = rightChild