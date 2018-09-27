from fractions import Fraction
import random

###################   Functions  ########################

def isEven(arg):
	if arg % 2 == 0:
		return True
	else:
		return False

def randRFact():
	randomR = random.random()
		
	rFact = Fraction(randomR).limit_denominator(5)
	
	while rFact == 1 or rFact.denominator - rFact.numerator <= 1:
		randomR = random.random()
		rFact = Fraction(randomR).limit_denominator(5)
	
	return rFact