#Table of a given Number.

i=int(input("Enter the number whose table is required: "))
print("TABLE OF ",i)
for j in range (1,11):    #Loop for multiplication.
	#print(i,"    X","    ",j,"    =","    ",i*j)
	print("{}\tX\t{}\t=\t{}".format(i,j,i*j))
	

