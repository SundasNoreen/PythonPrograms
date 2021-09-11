#Registration Number: 2019-CE-3
#Name: Sundas Noreen
#Program to Count Leters and Digits in a string.
 
Input_String= input("Enter a String : ")    #Prompt the user to enter a string.
letters=0                                   #Initializing to zero.
digits=0
upper=0
lower=0

for i in range(len(Input_String)):          #Loop upto the length of the string.
    if(Input_String[i].isalpha()):          #checking either it is alphabet or not.
       letters =letters + 1                 #if yes,then increment number of letters by 1.
       if(Input_String[i].isupper()):       #checking either it is uppercase or not.
           upper=upper+1                    #if yes,then increment number of uppercase letters by 1.
       else:
           lower=lower+1                    #if not,then increment number of lowercase letters by 1.
    elif(Input_String[i].isdigit()):        #checking either it is a digit or not.
        digits = digits + 1                  #if yes,then increment number of digits letters by 1.
  
print("\nTotal Number of Characters in this String :  ", len((Input_String)))  
print("\nTotal Number of Digits in this String :  ", digits)     
print("\nTotal Number of Alphabets in this String :  ", letters)
if letters!=0:                       #If there are no letters then, no need to display upper or lower case.
    print("\n    Total Number of Upper-case Alphabets in this String :  ", upper)
    print("\n    Total Number of lower-case Alphabets in this String :  ", lower)
if letters==0:
    print("\n    NO upper-case or lower-case alphabets exists.")