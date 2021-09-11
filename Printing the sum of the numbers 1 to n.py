#Write a program that asks the user for a number n and prints the sum of the numbers 1 to n.
x=int(input("Enter a number: "))
sum=0
for i in range (1,x+1,1):
    sum=sum+i
print (sum)


#Modify the previous program such that only multiples of three or five are 
#considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
y=int(input("Enter a number: "))
total=0
for j in range (3,y+1,1):
    if j%3==0 or j%5==0:
        total=total+j
print (total)
