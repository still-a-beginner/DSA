#FIFO is : First in First out method.

#Queue object has a constructor which is a list.
class Queue(object):
    
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return self.queue == []
    
    #Enqueue is to append data.
    def enqueue(self,data):
        self.queue.append(data)
        
    #Dequeue is to remove the data.
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    #Peek is to look at the top most item
    def peek(self):
        return self.queue[0]
    
    #Size of the queue is the length of the list of the constructor
    def sizeQueue(self):
        return len(self.queue)
        
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(3)
q.enqueue(34)
print(q.sizeQueue())
print("Dequeue", q.dequeue())
