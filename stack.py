#Stack follows LIFO : Last in First out method.

#Stack object has a constructor which is an array/list itself.
class Stack(object):
    #Initialize the structure of stack.
    def __init__(self):
        self.stack = []
    
    #Check if the stack is empty or not using boolean.
    def isEmpty(self):
        return self.stack == []
    
    #Push is to append in the list
    def push(self,data):
        self.stack.append(data)
        
    #Pop is to remove the top most or most recently added item.
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    #Peek is to give the top most item in a stack.
    def peek(self):
        return self.stack[-1]
        
    #Size of stack is the same as the length of the array object in the Stack constructor
    def sizeStack(self):
        return len(self.stack)
        
s = Stack()
s.push(1)
s.push(3)
s.push(90)
s.push(12)
print(s.sizeStack())
print("Popped",s.pop())
print(s.peek())
print("Popped",s.pop())
print(s.sizeStack())
