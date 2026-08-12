class BinayTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
        
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been inserted"
    
    def searchNode(self, NodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == NodeValue:
                return "Success"
        return "Not found"
        
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])
            
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"
        return "Failed to delete"
        
newBT = BinayTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))
print(newBT.insertNode("Cola"))
newBT.levelOrderTraversal(1)