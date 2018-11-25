# Check if a binary tree is subtree of another binary tree 

from queue import Queue 
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		
class binaryTree:
	def __init__(self):
		self.root = None
		
	def insert(self, val):
		newNode = Node(val)
		if self.root == None:
			self.root = newNode
			
		else:
			temp = self.root
			while(True):
				if val < temp.val:
					if temp.left == None:
						temp.left = newNode
						break
					temp = temp.left
				else:
					if temp.right == None:
						temp.right = newNode
						break
					temp = temp.right
					
					
	def printTree(self):   # print row by row
		if self.root == None:
			return 
		
		q = Queue()
		temp = self.root
		q.put(temp)
		q.put(',')
		prev = False
		while(not q.empty()):
			item = q.get()
			if item == ',':
				if prev == False:
					q.put(',')
					prev = True
					print(item, end=' ')
			else:
				print(item.val, end= ' ')
				if item.left != None:
					q.put(item.left)
					prev = False
				if item.right != None:
					q.put(item.right)
					prev = False
					
		
		print('\n')
		
	def findRoot(self):
		return self.root
		
def isIdentical(t1, t2):
	if t1 == None and t2 != None:
		return False
	if t1 != None and t2 == None:
		return False
		
	if t1 == None and t2 == None:
		return True
		
	return (t1.val == t2.val) and isIdentical(t1.left, t2.left) and isIdentical(t1.right, t2.right)
	
	
def isSubTree(t1, t2):
	
	if t2 == None:
		return False
	
	if t1 == None:
		return False
		
	if isIdentical(t1, t2):
		return True
		
	return isSubTree(t1.left, t2) or isSubTree(t1.right, t2)
		
						
bT = binaryTree()
bT.insert(5)
bT.insert(2)
bT.insert(0)
bT.insert(9)
bT.insert(9)
bT.insert(8)

bT.printTree()

sT = binaryTree()
sT.insert(9)
sT.insert(8)
sT.insert(9)
sT.printTree()

print(isSubTree(bT.findRoot(), sT.findRoot()))