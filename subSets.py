

# Find the subset of items in a list with unique set of numbers
	
result = [[]] 
def findSubsets(llist, index, subSet):
	for i in range(index, len(llist)):
		print(i)
		result.append(subSet+[llist[i]])
		findSubsets(llist, i+1, subSet+[llist[i]])
llist = [1,2,3]
findSubsets(llist, 0 , [])	
print(result)