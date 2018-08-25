# Here we have a maze matrix that we want to read in and creat a graph
# This matrix has m x n cells (nodes) that are given to use
# m: the number of rows, and n: the number of columns
# graph's nodes are zero-indexed
graph = {}

matrix = [['|+|+|+|+|+|+|'],
          ['|- - - -|- -|'],
          ['|- - -|- - -|'],
          ['|- - - - -|-|'],
          ['|- -|- - - -|'],
          ['|+|+|+|+|+|+|']]

m = 4
n = 6

for i in range(m):
    for j in range(n):
        node = i*n + j
        graph[node] = []
        row = i + 1
        col = (node % n)*2 + 1

        if matrix[row][0][col+1] != '|':     
            temp = col + 2
            neigh = node + 1

            while temp < len(matrix[row][0]):  # to get the length of each string
                if matrix[row][0][temp + 1] == '|':
                    graph[node].append(neigh)
                    break
                temp += 2
                neigh += 1
        if matrix[row][0][col-1] != '|':
            temp = col - 2
            neigh = node - 1
            while temp >= 0:
                if matrix[row][0][temp - 1] == '|':
                    graph[node].append(neigh)
                    break
                temp -= 2
                neigh -= 1

        temp = row + 1
        neigh = node + n
        while temp < len(matrix) - 1:
           
            if matrix[temp][0][col] == '|' or matrix[temp][0][col] == '+':
                break
            if matrix[temp+1][0][col] == '|' or matrix[temp+1][0][col] == '+':
                graph[node].append(neigh)
                break
            temp += 1
            neigh += n

        temp = row - 1
        neigh = node - n
        while temp > 0:
            
            if matrix[temp][0][col] == '|' or matrix[temp][0][col] == '+':
                break
            if matrix[temp-1][0][col] == '|' or matrix[temp-1][0][col] == '+':
                graph[node].append(neigh)
                break
            temp -= 1
            neigh -= n


for node, neighs in graph.items():
    print(node, ':', neighs)
            
