def spiral(num):
	# keep row increase col
	# keep col increase row
	# keep row decrease col
	# keep col decrease row
	
	matrix = [['' for i in range(num)] for j in range(num)]
	i = 0
	j = 0
	maxRow = num - 1
	minRow = 0
	maxCol = num - 1
	minCol = 0
	current = 0
	
	while current < (num*num):
			
		while(j <= maxCol):
			current += 1
			matrix[i][j] = current
			j += 1
			
		minRow += 1
		j -= 1
		i += 1
	
		##################################
		
		while(i <= maxRow):
			
			current += 1
			matrix[i][j] = current
			i += 1
		
		maxCol -= 1
		i -= 1
		j -= 1
			
		##################################
		
		while(j >= minCol):
			current += 1
			matrix[i][j] = current
			j -= 1
		
		maxRow -= 1
		i -= 1
		j += 1
		
		##################################
			
		while(i >= minRow):
			current += 1
			matrix[i][j] = current
			i -= 1
			
		minCol += 1
		j += 1
		i += 1
		##################################
		
	
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print (matrix[i][j], end = ' ')
		print('\n')
		
	print('_____________________________________\n')
	

spiral(3)
spiral(4)	
spiral(5)
spiral(6)
spiral(7)
		

		
	
	
	
	