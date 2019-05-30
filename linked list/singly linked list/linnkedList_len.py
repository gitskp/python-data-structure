class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head= None


	def insertBegin(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def count_list(self):
		temp = self.head
		count=0
		while temp!=None:
			count+=1
			temp = temp.next
		return count





llist = LinkedList()
llist.insertBegin(1)
llist.insertBegin(3)
llist.insertBegin(1)
llist.insertBegin(2)
llist.insertBegin(1)
print("Total number of node in LinkedList:",llist.count_list())