#Importing the library
from collections import deque

#Creating a Queue
queue = deque([1,5,8,9])

#Enqueuing elements to the Queue
queue.append(7) #[1,5,8,9,7]
queue.append(0) #[1,5,8,9,7,0]

#Dequeuing elements from the Queue
queue.popleft() #[5,8,9,7,0]
queue.popleft() #[8,9,7,0]

#Printing the elements of the Queue
print(queue)
