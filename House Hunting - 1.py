#House Hunting:You have graduated from UET and now have a great job! You move to Lahore and decide that you want to start saving to buy a house.


Annual_Salary=float(input("Enter your annual Salary: "))                        #Asking Annual Salary from the user.
Portion_Saved=float(input("Enter the percentage of salary to be saved: "))      #Asking about the portion of the monthly salary user saves.
Total_Cost=float(input("Enter the cost of your dream home: "))                  #Asking the user for the Whole Cost of his dream house.

Portion_Down_Payment=(Total_Cost*25)/100            #Portion Down Payment of the house is 25% of the Entire Cost of the house.


Monthly_Salary=Annual_Salary/12
Amount_of_Portion_Saved=(Portion_Saved*Monthly_Salary)/100      #Amount of the money saved by the user monthly.
                                            
r=0.04                                                          #Annual return rate from Investments. i.e.,4% or 0.04   


count=0                                                         #Counting the number of months.
Current_Savings=0.0                                             #The user is starting from Zero.
while Current_Savings<Portion_Down_Payment:                     #Until you have much money for Portion Down Payment.

    Current_Savings=Current_Savings+Current_Savings*(r/12)     #Every month your Savings increases by the amount of return from installments.
    Current_Savings=Current_Savings+Amount_of_Portion_Saved    #The portion of money you saves from your monthly income also adds up to your savings.
    count=count+1                                              #Each time the loop runs, increment the number of months by One.
    
print("\nNumber of Months you require to save amount for Portion Down Payment are: " ,count) #Print the number of months.