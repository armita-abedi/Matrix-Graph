'''
Add two numbers in the format of linked list:

**Input:**
First Number     : 351            0->3->5->1
Second Number    : 2249           2->2->4->9 

**Output:**
Correct Addition : 2600           2->6->0->0


Plus: reverse a linked list recursively
'''

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head = None
		
	def insert(self, val):
		newNode = Node(val)
		if self.head == None:
			self.head = newNode
		else:
			temp = self.head
			while(temp.next):
				temp = temp.next
				
			temp.next = newNode
			
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.val, end = ' -> ')
			temp = temp.next
			
		print('None\n')
		
	def findHead(self):
		return self.head
		
		
	def getLength(self):
		length = 0
		temp = self.head
		while(temp):
			length += 1
			temp = temp.next
		return length


	
	
	
def addLeadingZeros(llist1,llist2):
	h1 = llist1.findHead()
	h2 = llist2.findHead()
	
	length1 = llist1.getLength()
	length2 = llist2.getLength()
	
	if length1 < length2:
		diff = length2 - length1
		for d in range(diff):
			newNode = Node(0)
			newNode.next = h1
			h1 = newNode
	elif length1 > length2:
		diff = length1 - length2
		for d in range(diff):
			newNode = Node(0)
			newNode.next = h2
			h2 = newNode
		
	temp = h1
	while(temp):
		print(temp.val, end = ' -> ')
		temp = temp.next
			
	print('None\n')
	
	temp = h2
	while(temp):
		print(temp.val, end = ' -> ')
		temp = temp.next
			
	print('None\n')
	return h1,h2
		
		
		
def addition(llist1, llist2):

	head1, head2 = addLeadingZeros(llist1,llist2)
	
	def add2Numbers(head1,head2):
	

		if head1 == None and head2 == None:
			return None, 0
	
		nnode = Node(0)
		tup = add2Numbers(head1.next, head2.next)
		nnode.next = tup[0]
		temp = head1.val + head2.val + tup[1]
		if temp >= 10:
			q = temp - 10
			carry = 1
		else:
			q = temp
			carry = 0
		nnode.val = q
		return nnode, carry
	
	return add2Numbers(head1,head2)

print('\n____________________________\n')		
llist = LinkedList()
llist.insert(9)
llist.insert(2)
llist.insert(3)
llist.insert(0)
llist.insert(2)
llist.printList()


llist2 = LinkedList()
llist2.insert(9)
llist2.insert(0)
llist2.insert(0)
llist2.insert(8)
llist2.printList()


tup  = addition(llist, llist2)

if tup[1] > 0:
	headResult = Node(tup[1])
	headResult.next = tup[0]
else:
	headResult = tup[0]
	
while(headResult):
	print(headResult.val, end = ' -> ')
	headResult = headResult.next
			
print('None\n')



def reverse(head, newHead, length):
	if head.next == None:
		newHead = head
		return head, newHead, length+1
		
	trip = reverse(head.next, newHead, length)
	temp = trip[0]
	temp.next = head
	return head, trip[1], trip[2]+1
	
print('\n____________________________\n')	
llist.printList()
hLlist = llist.findHead()
trip = reverse(hLlist, None, 0)
temp = trip[1]
length = trip[2]
# add null to the end
hLlist.next = None
headResult = temp
while(headResult):
	print(headResult.val, end = ' -> ')
	headResult = headResult.next
print('None\n')