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
        
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)
        
newBT = BinayTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))
print(newBT.insertNode("Cola"))
newBT.preOrderTraversal(1)