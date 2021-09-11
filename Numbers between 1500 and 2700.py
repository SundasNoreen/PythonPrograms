#Python program to find and display those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700.

print("The numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 are:")

for i in range(1500,2701,1):
    if i%7==0 and i%5==0:
        print(i)