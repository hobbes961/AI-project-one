


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