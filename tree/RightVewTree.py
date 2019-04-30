class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right= None

def rightview_tree(root,level,max_level):
	if root is None:
		return
	if max_level[0]<level:
		print(root.data,end=" ")
		max_level[0] = level
	rightview_tree(root.right,level+1,max_level)
	rightview_tree(root.left,level+1,max_level)

def rightview(root):
	max_level = [0]
	rightview_tree(root,1,max_level)
	



root = Node(12)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)
rightview(root)