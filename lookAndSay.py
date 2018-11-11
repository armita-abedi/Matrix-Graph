'''
Implement a function that outputs the Look and Say sequence:
1 
11
21
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211
'''


def lookSay(numRows):
	currentList = [1]
	counter = 1
	print(currentList)
	while(counter < numRows):
		result = []
		cnt = 0
		prev = currentList[0]
		for i in range(len(currentList)):	
			
			if prev == currentList[i]:
				cnt += 1
			else:
				result.append(cnt)
				result.append(prev)
				prev = currentList[i]
				cnt = 1
			if i == len(currentList) - 1:
				result.append(cnt)		
				result.append(currentList[i])	
				
				
		counter += 1
		print(result)
		currentList = result
		
		
lookSay(10)