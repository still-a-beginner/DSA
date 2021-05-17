class Node(object):
    
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild = None
        
class BinarySearchTree(object):
    
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)
    
    def insertNode(self,data,node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)
    
    def remove(self,data):
        if self.root:
            self.root = self.removeNode(data, self.root)
            
    def removeNode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("Removing leaf")
                del node
                return None
            if not node.leftChild:
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                tempNode = node.leftChild
                del node
                return tempNode
            tempNode = self.getPred(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data,node.leftChild)
        return node
                        
        def getPred(self, node):
            if node.rightChild:
                return self.getPred(node.rightChild)
            return node
            
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)
    
    def getMin(self,node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        return node.data
        
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
    
    def getMax(self,node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data
        
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)
    
    def traverseInOrder(self,node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        print(node.data)
        if node.rightChild:
            self.traverseInOrder(node.rightChild)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)
bst.traverse()
print()
print(bst.getMaxValue())
print(bst.getMinValue())
print()
bst.remove(5)
bst.traverse()
