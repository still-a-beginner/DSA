#The linkedlist is useful in many places. It has  afew disadvantages and advantages over lists
#Insert/Remove item at the beginning: linkedlist Θ(1) time complexity. Use linkedlists.
#Insert/Remove item at the end or any other point: linkedlist Θ(len(l)) time complexity Use arrays.

#The node object consists of a constructor node which has a data and reference initially.
class Node(object):
    def __init__(self,data):
        self.data = data
        self.nextNode = None

#The linkedlist object has a constructor which has a reference head and size initially
class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None
    
    #Use linkedlist to insert data at the start of the object. It has time complexty of Θ(1).
    #A new node of Node object type with data is made in inserting in linkedlist.
    def insertStart(self,data):
        self.size = self.size + 1
        newNode = Node(data)
        
        #Reference f the node is made below.
        #If the linkedlist is initially empty then the there is no next node. So make a node to refer to the null or none value.
        if not self.head:
            self.head = newNode
        
        #Else the linkedlist is non empty then the 
        else:
            newNode.nextNode = self.head
            self.head = newNode
    
    #The size of the linkedlist is returned
    def size(self):
        return self.size
