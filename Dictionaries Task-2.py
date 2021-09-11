#   Lab Assignemnt on "DICTIONARIES" 
#   Task 2
#   Submitted By: 2019-CE-3 (SUNDAS NOREEN)

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Add the key to the inventory called ‘pocket’ to be a list containing strings 'seashell’, ‘strange berry’, and 'lint'.
inventory["pocket"] =  ["seashell", "strange berry", "lint"]

print("\nThe key 'pocket' is:")
print("inventory['pocket']: ",inventory["pocket"])


# Sorting the items in the list stored under the 'backpack' key.
inventory["backpack"].sort()

print ("\nKey 'Backpack' after Sorting becomes:")
print(inventory["backpack"])

# Now removing ‘dagger’ from the key 'backpack'.
inventory["backpack"].remove("dagger")

print("\nKey 'backpack' after removing 'dagger' becomes:")
print(inventory["backpack"])

# Adding '50' to the number stored in gold key.
inventory["gold"] =inventory["gold"]+ 50

print("\nThe Key 'gold' now becomes:" )
print(inventory["gold"])