'''
Athreya Murali
calcCantor.py

This program finds the partial sum of the Cantor Dust in a Cantor Set C, given a randomized r-factor
'''

################ Import Statements #######################

from fractions import Fraction

import math

# customized modules
import cantor
import fractionTest

################ Constants/ Global Variables #######################

# generate r-factor
rFact = fractionTest.randRFact()

# limit on iterations
#LIMIT = 3

# print statement
# print "\nTHIS IS THE SUMMATION OF THE CANTOR SET WITH"
# print "R-Factor: " + str(rFact) + "\n"

################ Summation Function #######################

# designed off of summation equation for Cantor ternary Set
def summateR(limit):	
	sumR = 0
	remainder = rFact.denominator - rFact.numerator
	for i in range(0,limit):		
				
		# the amount of space removed, based on the r-factor and the number of line segments removed in iteration
		iterRemvd = rFact.numerator * math.pow(remainder, i) 
		
		# proportional to the length of spaces removed
		iterLength = math.pow(rFact.denominator, i + 1)
			
		removed = iterRemvd / iterLength
				
		sumR += removed

	return sumR


################ Calculations #######################
#print "\n\n"

# loop until a math overflow is imminent, limit reached on number of calculations
# i = 0
# while True:
# 	try:
# 		summation = summateR(i)
# 	except (OverflowError):
# 		print "\n"
# 		break
# 	else:
# 		print "For Iteration {0}, The total Cantor Dust Length is: {1:.16f}".format(i, summation)
# 		i += 1

# for i in range(50):
# 	try:
# 		summation = summateR(i)
# 	except (OverflowError):
# 		print "\n"
# 		break
# 	else:
# 		print "For Iteration {0}, The total Cantor Dust Length is: {1:.16f}".format(i, summation)
# 
# print "\n"
################ L-system #######################

# grammars and seed for L-system based on r-factor
'''
one = cantor.genOnes(rFact)
zero = cantor.genZeroes(rFact)
seed = [1]

cantor.rewrite(seed, one, zero, 0, LIMIT)
'''