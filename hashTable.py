
class Item:
	def __init__ (self, val):
		self.val = val
		self.next = None
		
class Table:
	def __init__ (self):
		self.size = 11
		self.tbl = [None for i in range(self.size)]
		
	
	def search_item(self, val):
		cell = val % self.size
		current = self.tbl[cell]
		while(current != None):
			if current.val == val:
				return True
			current = current.next
			
		return False
		
	def add_item(self, val):
		if self.search_item(val):
			print ("Item " + str(val) + " already exists!\n")
			return
			
		cell = val % self.size
		newItem = Item(val)
		if self.tbl[cell] == None:
			self.tbl[cell] = newItem
		else:
			current = self.tbl[cell]
			while(current.next != None):
				current = current.next
				
			current.next = newItem
		
	def delete_item(self, val):
		if not self.search_item(val):
			print("Item " + str(val) + " does not exist!\n")
			return
		cell = val % self.size
		
		
		prev = None
		current = self.tbl[cell]
		if self.tbl[cell].val == val:
			self.tbl[cell] = self.tbl[cell].next
			return
		while(current != None):
			if current.val == val:
				prev.next = current.next
				return
			prev = current
			current = current.next
			
	def print_table(self):
		for i in range(self.size):
			if self.tbl[i] != None:
				current = self.tbl[i]
				while(current != None):
					print(current.val, end=' ')
					current = current.next
				print('\n')
			
		
		
hashTable = Table()
hashTable.add_item(6)
hashTable.add_item(7)
hashTable.add_item(6)
hashTable.add_item(22)
hashTable.add_item(33)
hashTable.add_item(16)
hashTable.add_item(18)
hashTable.print_table()
hashTable.delete_item(33)
hashTable.print_table()
		
			
			
		