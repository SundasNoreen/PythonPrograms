#This script will determine how long it will take to save for the house if your salary increases semi-annualy.
#Increase salary by the semi annual raise at 6 months, 12 months, and 18 months, etc. 

Annual_Salary=float(input("Enter your annual Salary: "))                        #Asking Annual Salary from the user.
Portion_Saved=float(input("Enter the percentage of salary to be saved: "))      #Asking about the portion of the monthly salary user saves.e.g.,10,20 etc.
Total_Cost=float(input("Enter the cost of your dream home: "))                  #Asking the user for the Whole Cost of his dream house.
Semi_Annual_Raise = float(input('Enter your 6-monthly raise as a decimal of your current salary:')) #Six Month Raise in Salary in %age.e.g., 3,4 etc.
                                                                                     

Portion_Down_Payment = (Total_Cost*25)/100           #Portion Down Payment of the house is 25% of the Entire Cost of the house.
Current_Savings = 0                                  #The user is starting from Zero.


r=0.04                                           #Annual return rate from Investments. i.e.,4% or 0.04  
Monthly_Salary=Annual_Salary/12                  
Amount_of_Portion_Saved=(Portion_Saved*Monthly_Salary)/100      #Amount of  money saved by the user monthly.    

Count = 0                                                       #Counting the number of Months.
while Current_Savings < Portion_Down_Payment:                   #Until you have much money for Portion Down Payment.
    if Count != 0 and Count%6 == 0:                             #Checking for the semi-annual raise.
        Annual_Salary=Annual_Salary *(1+(Semi_Annual_Raise)/100)
        Monthly_Salary=Annual_Salary/12
        Amount_of_Portion_Saved=(Portion_Saved*Monthly_Salary)/100
    Current_Savings =Current_Savings+Amount_of_Portion_Saved +(Current_Savings*r)/12
    Count += 1               #Each time the loop runs, increment the number of months by One.
  
print("\nNumber of Months you require to save amount for Portion Down Payment are: " ,Count)   #Print the number of months.