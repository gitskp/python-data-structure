''' Logic:
(1) When calling the enqueue method, simply push the elements into the stack 1.
(2) If the dequeue method is called, push all the elements from stack 1 into stack 2, which reverses the order of the elements. Now pop from stack 2.'''

class Queue(object):
    def __init__(self):
        self.instack=[]
        self.outstack=[]
    def enqueue(self,element):
        self.instack.append(element)
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
q=Queue()
for i in range(10):
    q.enqueue(i)
for i in range(10):
    print (q.dequeue())
