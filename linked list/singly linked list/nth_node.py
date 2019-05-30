class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None


	def insertBegin(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def nth_node(self,n):
		current = self.head
		count=0
		while current!=None:
			count+=1
			if count==n:
				return current.data
			current = current.next





llist = LinkedList()
llist.insertBegin(1)
llist.insertBegin(3)
llist.insertBegin(4)
llist.insertBegin(5)
llist.insertBegin(10)

n = 4
print ("Element at index is :", llist.nth_node(n)) 