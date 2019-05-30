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


	def searchNode(self,x):
		current = self.head
		while current != None:
			if current.data == x:
				return True
			current = current.next
		return False

llist = LinkedList()
llist.insertBegin(1)
llist.insertBegin(3)
llist.insertBegin(4)
llist.insertBegin(5)
llist.insertBegin(10)


if llist.searchNode(5):
	print("yes")
else:
	print("No")
