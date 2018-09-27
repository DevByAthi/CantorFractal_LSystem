'''
Athreya Murali
cantor.py

Generates appropriate L-system and L-system grammars for a Cantor Set C based on a given r-factor
'''

###################  Print Functions  ##########################

# prints each element of array on its own line (used during debugging)
def printArr(arr):
	# prints each element in arr
	for i in arr:
		print i
	
	# line break
	print "\n"

# makes string to print output array's last iteration more cleanly (used during debugging)
def arrString(arr):
	newString = ""
	for i in arr:
		newString += str(i)
	return newString

###################  Generate Arrays  ##########################

# generate ones grammar
def genOnes(rFact):
	# length of the array representing the Ones grammar
	numElems = rFact.denominator
	
	# how many zeroes will be in the middle of the grammar
	numZeroes = rFact.numerator
	
	# how many ones total will be in the Ones grammar
	numOnes = numElems - numZeroes
	
	ones = []
	
	# calculate how many ones are on each side for a Cantor Set 'type C'
	# sides are the number of ones on each side in the Ones grammar
	if (numOnes % 2 == 0):
		side1 = numOnes / 2
		side2 = numOnes / 2
	else:
		side1 = (numOnes - 1) / 2
		side2 = numOnes - side1
	
	# append ones and zeroes in appropriate order based on side1 and side2	
	for i in range(side1):
		ones.append(1)
	
	for j in range(numZeroes):
		ones.append(0)
	
	for k in range(side2):
		ones.append(1)	
	
	return ones


# generate zeroes grammar based on denominator of r-factor
def genZeroes(rFact):
	zeroes = [0 for i in range(rFact.denominator)]
	return zeroes

###################  Recursive Function  ##########################

# recursive function rewrite
'''
	@param arr- input array
	@param one- the array representing the Ones grammar
	@param zero- the array representing the Zeroes grammar
	@param iter- the current iteration of the Cantor Set
	@param limit- the maximum number of iterations allowed (included as a parameter to avoid the use of a global variable)
	
	@result: rewrite(arr2) OR L-system at given iteration limit
	
	base case: if iterated LIMIT number of times
	
	Loops through input array, appending L-system string
	depending on current value of input array index.
	repeats until iterated LIMIT times.
'''
def rewrite(arr, one, zero, iter, limit):
	
	# base case
	if iter == limit:
		return arr
	
	# blank output array, cleared every iteration of rewrite()
	arr2 = []
	
	# loops through input array
	for i in arr:
		# if val is 0, use L-system alphabet for 0
		if i == 0:
			for j in zero:
				arr2.append(j)
		# if val is 1, use L-system alphabet for 1
		else:
			for j in one:
				arr2.append(j)
	
	# outputs L-system
	# print "For iteration {0}:\n{1}".format(iter, arrString(arr))
# 	print "\n"
	
	# recursive return statement, using output array as input
	return rewrite(arr2, one, zero, iter + 1, limit)