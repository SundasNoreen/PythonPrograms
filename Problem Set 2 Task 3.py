# Programming Fundamentals
# Problem Set 2
# Submitted By: Sundas Noreen 
# Task 3
# To Find Largest number of McNuggets that cannot be bought in exact quantity.

print("\nProblem Set 2, Task 3")


def My_Function(n):                             # Defining a function that takes the total number of Nuggets as argument.
    a = 0
    b = 0
    c = 0
    for a in range(10):                         # Iterating over all Possible Combinations.
        if 6 * a + 9 * b + 20 * c == n:
            return 1
        for b in range(10):
            if 6 * a + 9 * b + 20 * c == n:
                return 1
            for c in range(10):
                if 6 * a + 9 * b + 20 * c == n:
                    return 1
    return 0

n=1                                             # Taking a start at n=1
flag=0                                          # Counter to keep track.
last_num=0

while flag<6:                               # Checking for the Six Consecutive values that pass the Exact Solution.
    if My_Function(n):
        flag=flag+1
    else:
        last_num=n
        flag=0
    n=n+1
   
print("\n",last_num,"is the largest number of nuggets that can not be ordered in a 6,9,20 combination.")




