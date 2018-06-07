'''Stack implementation using List

Here we are going to define a class Stack and add methods to perform the below operations:

    Push elements into a Stack
    Pop elements from a Stack and issue a warning if it’s empty
    Get the size of the Stack
    Print all the elements of the Stack'''

'''class Stack:
    def __init__(self):
        self.stack = list()
    #Adding elements to stack
    def push(self,data):
        #Checking to avoid duplicate entries
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False

    #Removing last element from the stack
    def pop(self):
        if len(self.stack)<=0:
            return ("Stack Empty!")
        return self.stack.pop()

    #Getting the size of the stack
    def size(self):
        return len(self.stack)

myStack = Stack()
print(myStack.push(5)) #prints True
print(myStack.push(6)) #prints True
print(myStack.push(9)) #prints True
print(myStack.push(5)) #prints False since 5 is there
print(myStack.push(3)) #prints True
print(myStack.size())  #prints 4
print(myStack.pop())   #prints 3
print(myStack.pop())   #prints 9
print(myStack.pop())   #prints 6
print(myStack.pop())   #prints 5
print(myStack.size())  #prints 0
print(myStack.pop())   #prints Stack Empty!'''



'''........................................................................................'''

'''Stack implementation using Array

Python Lists have made it so easy to implement Stack. However, if you want to implement Stack language agnostically, you have to assume that lists are like arrays (fixed in size) and use a Top pointer to keep a tab on the status of the stack. Check this animation to understand how it works.
Algorithm

    Declare a list and an integer MaxSize, denoting the maximum size of the Stack
    Top is initially set to 0
    Push operation:
        Check if Top is less than the MaxSize of the Stack
            If yes, append data to stack and increment top by 1
            If no, print stack full message
    Pop operation:
        Check if Top is greater than 0:
            If yes, pop the last element from the list and decrement top by 1
            If no, print stack empty message
    Size operation:
        The value of the Top pointer is the size of the Stack
'''

class Stack:

    #Constructor
    def __init__(self):
        self.stack = list()
        self.maxSize = 8
        self.top = 0

    #Adds element to the Stack
    def push(self,data):
        if self.top>=self.maxSize:
            return ("Stack Full!")
        self.stack.append(data)
        self.top += 1
        return True

    #Removes element from the stack
    def pop(self):
        if self.top<=0:
            return ("Stack Empty!")
        item = self.stack.pop()
        self.top -= 1
        return item

    #Size of the stack
    def size(self):
        return self.top

s = Stack()
print(s.push(1))#prints True
print(s.push(2))#prints True
print(s.push(3))#prints True
print(s.push(4))#prints True
print(s.push(5))#prints True
print(s.push(6))#prints True
print(s.push(7))#prints True
print(s.push(8))#prints True
print(s.push(9))#prints Stack Full!
print(s.size())#prints 8
print(s.pop())#prints 8
print(s.pop())#prints 7
print(s.pop())#prints 6
print(s.pop())#prints 5
print(s.pop())#prints 4
print(s.pop())#prints 3
print(s.pop())#prints 2
print(s.pop())#prints 1
print(s.pop())#prints Stack Empty!
