#Stack follows LIFO : Last in First out method. It has limited space unlike Heaps. It is faster than Heaps. 
#The space in CPU is not fragmented unlike Heaps where memory is fragmented. 
#Resizing of variables can not take place in Stacks but in Heaps, there can be resizing which can take place.
#Recursion takes place in stacks in memory.

#Stack object has a constructor which is an array/list itself.
class Stack(object):
    #Initialize the structure of stack.
    def __init__(self):
        self.stack = []
    
    #Check if the stack is empty or not using boolean.
    def isEmpty(self):
        return self.stack == []
    
    #Push is to append in the list. It has time complexity as Θ(1).
    def push(self,data):
        self.stack.append(data)
        
    #Pop is to remove the top most or most recently added item. It has time complexity as Θ(1).
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    #Peek is to give the top most item in a stack. It has time complexity as Θ(1).
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

#Recursion is to call the function again and again
#Integer is passed through the function.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#Using stack
def factorialStack(n):
    f = Stack()
    f.push(n)
    while n != 1 :
        n = n - 1
        f.push(n*f.peek())
        
    return f.peek()

print(factorial(5))
print(factorialStack(5))
