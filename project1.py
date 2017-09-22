import random
from anytree import Node, RenderTree
import time
from copy import copy, deepcopy
#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
class GridGen():
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


#2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

class evalsgrid:

	def __init__(self,grid,n):
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


		#lets me see the output

		for row in evalgrid:
			print(' '.join([str(elem) for elem in row]))

		print evaluation
		self.evaluation=evaluation

#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333



#call this, takes a grid and value of n. will do basic hill climbing
def basichill(grid, n):
	#part 3 basic hill climbing

	#number of attempts is a user input
	attempts = input("enter number of attempts:" )
	#evaluation over time, need this in report so we can plot how our evaluation improves over each step
	EOT=[]
	#I don't want to actually touch the grid copy, will use A as the store and B as the test
	agrid=deepcopy(grid)
	bgrid=deepcopy(grid)
	baseeval=evalsgrid(grid,n)
	start=time.clock()
	for x in range(attempts):
		xsqr=random.randrange(0,n)
		ysqr=random.randrange(0,n)
		value = random.randrange(1,n)

		#while loop: to prevent changing goal square
		while(xsqr==(n-1) and ysqr==(n-1)):
			xsqr=random.randrange(0,n)
			ysqr=random.randrange(0,n)

		#while loop: to make sure new move number is legal
		while (xsqr+value>n-1 and xsqr-value<0 and ysqr+value>n-1 and ysqr-value<0):
			value =random.randrange(1,n)

		#makes a change
		bgrid[xsqr][ysqr]=value

		#updates the what the current evaluation is
		oldeval=evalsgrid(agrid,n)

		#call evaluation on new grid
		neweval= evalsgrid(bgrid,n)

		#compares evaluation of the two grids
		#if new grid has greater than or equal to, of previous grid the new grid becomes the grid
		if (neweval.evaluation>=oldeval.evaluation):
			agrid=deepcopy(bgrid)
			EOT.append(neweval.evaluation)
			print "grid was changed"
		else:
			bgrid=deepcopy(agrid) 
			EOT.append(oldeval.evaluation)






	stop=time.clock()
	totaltime=(stop-start)
	finaleval=evalsgrid(agrid,n)
	print "original grid was"
	for row in grid:
		print(' '.join([str(elem) for elem in row]))
	print "evluation number was:" + str(baseeval.evaluation) 

	print "final grid is:"
	for row in agrid:
		print(' '.join([str(elem) for elem in row]))
	print "evaluation number is: " + str(finaleval.evaluation)

	print "total time is: " + str(totaltime)
	#display total time
	for x in range(attempts):
		print EOT[x]


	#in report provide plot of evaluation function over the course of changes
	#plot is averaged over at least 50 runs
	#report statistics for different puzzle sizes
#######################################################################################################################





x=GridGen()
print x.n
print x.grid[0][0]
test = evalsgrid(x.grid,x.n)
print test.evaluation
basichill(x.grid, x.n)
