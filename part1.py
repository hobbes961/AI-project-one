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

