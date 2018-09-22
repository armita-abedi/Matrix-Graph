from heapq import heappush, heappop
import sys


G = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
[4, 0, 8, 0, 0, 0, 0, 11, 0],
[0, 8, 0, 7, 0, 4, 0, 0, 2],
[0, 0, 7, 0, 9, 14, 0, 0, 0],
[0, 0, 0, 9, 0, 10, 0, 0, 0],
[0, 0, 4, 14, 10, 0, 2, 0, 0],
[0, 0, 0, 0, 0, 2, 0, 1, 6],
[8, 11, 0, 0, 0, 0, 1, 0, 7],
[0, 0, 2, 0, 0, 0, 6, 7, 0]]


def shortest_path(s, G):
	openList = []
	path = [[float('inf'), i, None] for i in range(len(G))]
	path[0] = [0, s, None]
	heappush(openList, path[0])
	
	while(openList):
		
		(pathval, index, parent) = heappop(openList)
		print(index)
		for node, val in enumerate(G[index]):
			
			if val != 0 and (pathval + val) < path[node][0]:
				print(index, node, val)
				
				path[node][0] = (pathval+val)
				path[node][2] = index
				heappush(openList, path[node])
				print(len(openList))
		print('______')		
				
	print(path)
	
shortest_path(0, G)
		