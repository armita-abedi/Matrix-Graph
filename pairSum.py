'''
Given an array of numbers in sorted order, 
count the pairs of numbers whose sum is less than X.
'''


def sumFinder(llist, X):
	sumTotal = 0
	i = 0 
	j = len(llist) - 1

		
	while(i < j):
		diff = X - llist[i]
		if llist[j] < diff:
			sumTotal += (j-i)
			i += 1
		else:
			j -= 1
			
	
	print(sumTotal)
	

llist = [1,2,5,6,7,8]
llist2 = [1,1,1,2,3,4,5,5,5,7,8]

sumFinder(llist, 9)
sumFinder(llist2, 9)