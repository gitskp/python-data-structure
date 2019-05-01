""" we have to maintain a horizontal distance of all the nodes from the root node and print the last node for each horizontal distance."""

class Node:
	def __init__(self,data):
		self.data = data
		self.hd= -1
		self.left = None
		self.right = None



def bottomView(root):
	if root is None:
		return
	Q =  []
	Map = dict()
	Q.append(root)
	while len(Q)>0:
		p = Q[0]
		del Q[0]
		hd = p.hd
		Map[hd] = p.data

		if p.left is not None:
			p.left.hd = hd-1
			Q.append(p.left)
		if p.right is not None:
			p.right.hd = hd+1
			Q.append(p.right)
	print("Bootom view of tree is:")
	print(sorted(list(Map.values())))







root =   Node(20); 
root.left =  Node(8); 
root.right =   Node(22); 
root.left.left =   Node(5); 
root.left.right =   Node(3); 
root.right.left =   Node(4); 
root.right.right =   Node(25); 
root.left.right.left =   Node(10); 
root.left.right.right =   Node(14); 
root.hd =0 
bottomView(root); 