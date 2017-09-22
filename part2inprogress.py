import random
from anytree import Node, RenderTree
#grid size user input
n = input("Enter grid size' :" )

#2d array to store grid
grid = [[0] * n for i in range(n)]

#generates random values for each spot in grid
for x in range (0,n):
	for y in range (0,n):
		value = random.randrange(1,n)
		
		#checks that a valid move can be made with given value/square
		#will generate a new number until a valid one works
		
		while (x+value>n-1 and x-value<0 and y+value>n-1 and y-value<0):
			value =random.randrange(1,n)

		grid[x][y]=value


#change final square to 0 to be goal.
grid[n-1][n-1]=0

#prints grid
for row in grid:
	print(' '.join([str(elem) for elem in row]))
print grid[0][4]
print grid[0][3]
#completed up to here

###############################################################################


# auxillary matrix starts all zero
auxmat= [[0]*n for i in range(n)]
array=[0]*n*n

#making a tree, each node is a# where # is the the square number, read left to right
array[0]= Node(0)

queue=[]
queue.append(0)
auxmat[0][0]=1


while(len(queue)>0):
	square=queue.pop(0)
	x= square//n
	y= square%n
	value=grid[x][y]

	#checking for legal moves of squares we havent been to
	if(x + value<n and auxmat[x+value][y]==0):
		child=(x+value)*n+y
		auxmat[x+value][y]=1
		queue.append(child)
		array[child]=Node(child,parent= array[square])

	if(x-value>-1 and auxmat[x-value][y]==0):
		child=(x-value)*n+y
		auxmat[x-value][y]=1
		queue.append(child)
		array[child]=Node(child,parent= array[square])
	if(y+value<n and auxmat[x][y+value]==0):
		child=x*n+y+value
		auxmat[x][y+value]=1
		queue.append(child)
		array[child]=Node(child,parent= array[square])
	if(y-value>-1 and auxmat[x][y-value]==0):
		child=x*n+y-value
		auxmat[x][y-value]=1
		queue.append(child)
		array[child]=Node(child,parent= array[square])

print array[24]


#############################################
#define evaluation grid
evalgrid= [[0] * n for i in range(n)]


#if auxmat[node] = 1, find depth in tree x+y*row, set evaulationgrid[node] = depth
#else evaluationgrid[node] = X
for x in range(n):
	for y in range(n):
		if (auxmat[x][y] ==1):
			evalgrid[x][y]=array[x*n +y].depth
		else:
			evalgrid[x][y]="X"



#if auxmat[goal] = 0, count all such nodes and set evaluation = -sum of all 0's
#else evaluation = evaluationgrid[goal]


if auxmat[n-1][n-1]==0:
	counter=0
	for x in range(n):
		for y in range(n):
			if (auxmat[x][y]==0):
				counter=counter+1
	evaluation= counter*-1
	print evaluation
else:
	evaluation=evalgrid[n-1][n-1]


for row in evalgrid:
	print(' '.join([str(elem) for elem in row]))
print evaluation


