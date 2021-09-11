#Write a program that asks the user to enter an integer and prints two integers, root and pwr,
#such that 1 < pwr < 6 and root**pwr is equal to the integer entered by the user.
#If no such pair of integers exists, it should print a message to that effect.

number = int(input("Enter a positive integer: "))
root = 1
pwr = 2
answer = False

while pwr < 6:
    while root <= number:
        if root**pwr == number:
            print("The root", root, "elevated to", pwr, "equals", number)
            answer = True
            break
        else:
            root += 1
    root = 1
    pwr += 1
if answer == False:
    print("There is no pair of integers in which root**pwr equals the input") 

