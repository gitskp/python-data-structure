'''Algorithm

    Declare a list and an integer MaxSize, denoting a virtual maximum size of the Queue
    Head and Tail are initially set to 0
    Size method
         Calculates the number of elements in the queue -> Size = Tail - Head
    Reset method:
        Resets Tail and Head to 0
        Creates a new Queue (initializes queue to a new list)
    Enqueue operation:
        Check if Size is less than the MaxSize:
            If yes, append data to Queue and then increment Tail by 1
            If no, print Queue full message
    Dequeue operation:
        Check if Size is greater than 0:
            If yes, pop the first element from the list and increment Head by 1
            If no:
                Call Reset method
                Print Queue empty message'''
class Queue:

    #Constructor
    def __init__(self):
        self.queue = list()
        self.maxSize = 8
        self.head = 0
        self.tail = 0

    #Adding elements
    def enqueue(self,data):
        #Checking if the queue is full
        if self.size() >= self.maxSize:
            return ("Queue Full")
        self.queue.append(data)
        self.tail += 1
        return True

    #Deleting elements
    def dequeue(self):
        #Checking if the queue is empty
        if self.size() <= 0:
            self.resetQueue()
            return ("Queue Empty")
        data = self.queue[self.head]
        self.head+=1
        return data

    #Calculate size
    def size(self):
        return self.tail - self.head

    #Reset queue
    def resetQueue(self):
        self.tail = 0
        self.head = 0
        self.queue = list()

q = Queue()
print(q.enqueue(1))#prints True
print(q.enqueue(2))#prints True
print(q.enqueue(3))#prints True
print(q.enqueue(4))#prints True
print(q.enqueue(5))#prints True
print(q.enqueue(6))#prints True
print(q.enqueue(7))#prints True
print(q.enqueue(8))#prints True
print(q.enqueue(9))#prints Queue Full!
print(q.size())#prints 8
print(q.dequeue())#prints 8
print(q.dequeue())#prints 7
print(q.dequeue())#prints 6
print(q.dequeue())#prints 5
print(q.dequeue())#prints 4
print(q.dequeue())#prints 3
print(q.dequeue())#prints 2
print(q.dequeue())#prints 1
print(q.dequeue())#prints Queue Empty
#Queue is reset here
print(q.enqueue(1))#prints True
print(q.enqueue(2))#prints True
print(q.enqueue(3))#prints True
print(q.enqueue(4))#prints True                
