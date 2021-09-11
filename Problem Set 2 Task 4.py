# Programming Fundamentals
# Problem Set 2
# Submitted By: Sundas Noreen (2019-CE-3)
# Task 4
# Using Tuples to test our program on a variety of choices of Package Sizes.

print("\nProblem Set 2, Task 4")

bestSoFar = 0       # Keeping track of largest number of McNuggets that cannot be bought in exact quantity.

Combination_1 = (6,9,20)              # Tuple that contain given Package Size of 6,9,20 that is given.
Combination_2= (5,10,14)              # Tuple that contains other combinations of Package sizes.
Combination_3 = (9,12,14)   
Combination_4= (20,12,9)   
Combination_5 = (15,8,6)   
Combination_6 = (21,15,19)   

Choices = (Combination_1,Combination_2,Combination_3,Combination_4,Combination_5,Combination_6)
test = len(Choices)

def is_n_solveable(n,packages):     # n is the total number of nuggets.          
	a = 0	                         # Initializing the multiples of each package size.
	b = 0
	c = 0
	for a in range(10):
		if packages[0]*a + packages[1]*b + packages[2]*c == n:
			return 1
		for b in range(10):
			if packages[0]*a + packages[1]*b + packages[2]*c == n:
				return 1
			for c in range(10):
				if packages[0]*a + packages[1]*b + packages[2]*c == n:
					return 1
	return 0

	
def Variety (packages): # Take Tuple as an argument and will check for highest number that cannot be bought in exact quantity.
	for n in range(1, 150):    
		if is_n_solveable(n, packages):
			bestSoFar = bestSoFar + 1
		else:
			bestSoFar = 0
            
		if bestSoFar == packages[0]:
			print ("\nGiven package sizes", packages[0], ",", packages[1], " and", packages[2], ", the largest number of McNuggets that cannot be bought in exact quantity is:", n-packages[0])
			
for i in range(test):                   #Checking all the Choices.
	Variety(Choices[i])
