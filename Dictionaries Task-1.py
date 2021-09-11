#   Lab Assignemnt on "DICTIONARIES" 
#   Task 1
#   Submitted By: SUNDAS NOREEN
#   A Python program to find the highest 4 values in a dictionary.


# Dictionary with respective keys and values.  
Dictionary = {'a': 35, 'b': 84, 'c': 46, 'd': 53, 'e': 98, 'f':100, 'g':120, 'h':21} 

# Sorting the given dictionary in descending order.
sorted_Dictionary = sorted(Dictionary.items(),key=lambda x: x[1], reverse=True)
print(sorted_Dictionary)

# For getting the highest 4 values, just print the first four elements of the Sorted List.

print("\nThe Given Dictionary is:")
print(Dictionary,"\n")

print("Highest 4 Values along with their keys are:")
print(sorted_Dictionary[0])
print(sorted_Dictionary[1])
print(sorted_Dictionary[2])
print(sorted_Dictionary[3])
