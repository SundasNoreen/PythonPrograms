#Program that prints the next 20 leap years.
x=int(input("Enter the Present year: "))
count=0
while count!=20:
    x=x+1
    if x%4==0 and x%100!=0:
        print(x) 
        count=count+1
    elif x%4==0 and x%100==0 :
        if x%400==0:
            print(x)
            count=count+1       
            
    
    
   
    
    
    