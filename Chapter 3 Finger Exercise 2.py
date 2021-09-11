s = (input("Enter some decimal numbers, separated by commas: "))
str_list = s.split(",")
total = 0

for i in  str_list:
    total +=float(i)

print("The sum of the decimal numbers entered is:", total) 

