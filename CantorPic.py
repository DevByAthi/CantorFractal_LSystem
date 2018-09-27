'''
Athreya Murali
CantorPic.py

Uses the output of cantor.py's rewrite function to generate the Cantor Fractal
using underscores and spaces

'''

import cantor
import fractionTest
import calcCantor

# generate random r-factor
rFact = fractionTest.randRFact()

# Iteration limit
LIMIT = 3

# Seed
seed = [1]

# Ones and Zeroes Grammars
ones = cantor.genOnes(rFact)
zeroes = cantor.genZeroes(rFact)

print "\nTHIS IS THE CANTOR FRACTAL WITH"
print "R-Factor: " + str(rFact) + "\n"

fractalNum = cantor.rewrite(seed, ones, zeroes, 0, LIMIT)

fractalPic = ""

for i in fractalNum:
	if i == 0:
		fractalPic = fractalPic + " "
	else:
		fractalPic = fractalPic + "_"

print fractalNum

print "\n\n"

print fractalPic