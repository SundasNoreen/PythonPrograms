#Chapter 2 Finger Exercise 3
#Print the largest Odd Integer.

numbers = []

# get user to input 10 integers
for i in range(0, 10):
    x=int(input("Enter an Integer: "))
    numbers.append(x)
    
    
# find largest odd number
max = 0
for y in numbers:
    if y % 2 != 0 and y > max:
        max = y
if max == 0:
    print ("There were no odd integers")
else:
    print ("\nThe Largest Odd Integer is: ",max)
        
