#The doublelinkedlist is where the reference of a node is in both the directions, forwards and backwards.
#The doublelinkedlist is useful in many places. It has  a few disadvantages and advantages over lists
#Insert/Remove item at the beginning: doublelinkedlist Θ(1) time complexity. Use linkedlists.
#Insert/Remove item at the end or any other point: doublelinkedlist Θ(len(l)) time complexity Use arrays.

#The node consists of a a constructor node which has a data and reference initially.
class Node(object):
    def __init__(self,data):
        self.data = data
        self.nextNode = None

#The linkedlist object which has a reference head and size initially
class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None
    
    #Use linkedlist to insert data at the start of the object. It has time complexty of Θ(1).
    #A new node of Node object type with data is made in inserting in linkedlist.
    def insertStart(self,data):
        self.size = self.size + 1
        newNode = Node(data)
        
        #If the linkedlist is initially empty then the there is no next node. So make a node to refer to the null or none value.
        if not self.head:
            self.head = newNode
        
        #Else the linkedlist is non empty then the 
        else:
            newNode.nextNode = self.head
            self.head = newNode
    
    #The size of the linkedlist is returned. Time complexity is Θ(1).
    def linkedlistsize(self):
        return self.size
    
    #A new node of Node object type with data is made in inserting in linkedlist.
    #Iterate till we get the None value. The time complexity is Θ(size_final). So use lists to enter an element at the end.
    def insertEnd(self,data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head
        
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
            
        actualNode.nextNode = newNode
        
    #Time complexity is Θ(size_final). Use lists to show the list of numbers.
    def traverse(self):
        actualNode = self.head
        while actualNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode
    
    #Time complexity is Θ(size_final)
    def remove(self, data):
        #If linkedlist is empty then use this.
        if self.head is None:
            return
        #For removing an item in linkedlist, size is decreased by 1.
        self.size = self.size - 1
        #Current node is 
        currentNode = self.head
        previousNode = None
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        #Data to be removed is the first item
        if previousNode is None:
            self.head = currentNode.nextNode
        #Data to be removed is non first item
        else:
            previousNode.nextNode = currentNode.nextNode
            
ll = LinkedList()
ll.insertStart(1)
ll.insertStart(3)
ll.insertEnd(12)
ll.insertEnd(4)
ll.insertEnd(34)
ll.insertEnd(57)
ll.insertStart(42)
ll.insertStart(19)
ll.traverse()
print("size is",ll.linkedlistsize())
ll.remove(3)
ll.remove(12)
print("size is",ll.linkedlistsize())
