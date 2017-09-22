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
