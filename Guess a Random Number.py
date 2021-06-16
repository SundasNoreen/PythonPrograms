#Python Program to guess a number between 1 to 9. 

import random                                           #Header File which contains Random number Generator Function.
random_int=random.randint(1,9)                          #randint function to generate a random integer inbetween the end values including them.

count=0
while count<5:
    num=int(input("Enter a random guess from 1 to 9: "))    #Prompt user to guess a number.
    if num==random_int:                                     #If user guess matches the random generated number.
        print("Successful, Well Guessed!!!")
        break
    count=count+1                                           #More Attempts
    if count==5:
         print("\nThe number was ",random_int)



