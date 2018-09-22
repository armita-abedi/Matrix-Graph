

G = [[0 for i in range(8)] for j in range(4)]
G[0][4] = 1
G[0][5] = 1
G[0][6] = 1
G[0][7] = 1
G[1][7] = 1
G[1][5] = 1
G[1][6] = 1
G[2][0] = 1
G[2][1] = 1
G[2][3] = 1
G[2][4] = 1
G[3][0] = 1
G[2][5] = 1

start = (0,0)
end = (3,7)


def find_a_path(G, start, end):
	
	myStack = list()
	myStack.append(start)
	path = []
	visited = []
	def find_recursive(G, end):
		if len(myStack) == 0:
			return False
			
		q = myStack.pop()
		path.append(q)
		if q == end:
			print(path)
			return True
		visited.append(q)
		
		options = []
		i,j = q
		if j+1 < 8 and G[i][j+1] != 1:
			options.append((i,j+1))
			
		if j-1 >= 0 and G[i][j-1] != 1:
			options.append((i,j-1))
			
		if i+1 < 4 and G[i+1][j] != 1:
			options.append((i+1,j))
			
		if i-1 >=0 and G[i-1][j] != 1:
			options.append((i-1,j))
			
		if i-1 >=0 and j-1 >=0 and G[i-1][j-1] != 1:
			options.append((i-1,j-1))
			
		if i-1 >=0 and j+1 < 8 and G[i-1][j+1] != 1:
			options.append((i-1,j+1))
			
		if i+1 < 4 and j-1 >= 0 and G[i+1][j-1] != 1:
			options.append((i+1,j-1))
			
		if i+1 < 4 and j+1 < 8 and G[i+1][j+1] != 1:
			options.append((i+1,j+1))
		
		for opt in options:
			if opt not in visited:
				myStack.append(opt)
				if find_recursive(G, end):
					return True
			
		
		path.pop()	
	find_recursive(G, end)	
find_a_path(G, start, end)		
		