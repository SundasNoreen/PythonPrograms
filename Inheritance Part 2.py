# Programming Fundamentals Lab
# Task on Inheritance (Part-2)
# Date: 18th August 2020
# Submitted By: 2019-CE-3 (Sundas Noreen)

class Publication:              # Class Publication.
    def __init__(self):         # Object Constructor.
        self.get_data()
        self.put_data()
    def get_data(self):         # This Function will take Data from User.
        self.title=input("\nEnter the Title: ")
        self.price=float(input("Enter the Price: "))
    def put_data(self):         # This Function will Print Data on Screen.
        print("\nTitle is: ",self.title)
        print("Price is: ",self.price)

class Sales:              # Class Sales, it is also a Base/Parent Class.
    def __init__(self):
        self.get_data()
        self.put_data()
    def get_data(self):
        self.list=[]            # A List that will take 3 inputs from Users.
        for i in range(1,4):    # Loop that will iterate 3 times to ask user for his inputs.
            x=float(input("Enter amount of Dollars Sale in Month "+str(i)+" : "))
            self.list.append(x)   # Append each Input to the end of the List.
    def put_data(self):
        print("The Dollar Sales for the Last Three Months are: ",self.list[0]," , ",self.list[1]," and ",self.list[2],".")

class Book(Publication,Sales):        # Multiple Inheritance, Inherited from both Publication and Sales.
    def __init__(self):
        self.get_data()
        self.put_data()
    def get_data(self):
        super().get_data()            # Super Function will automatically inherit the properties from its First Parent Class.
        super(Publication,self).get_data()  # Here, it will call all constructors after Publication.
        self.page=int(input("Enter the Page Count: "))
    def put_data(self):
        super().put_data()
        super(Publication, self).put_data()
        print("The Page Count is: ",self.page)
        print("______________________________________")

class Tape(Publication, Sales):        # Multiple Inheritance, Inherited from both Publication and Sales.
    def __init__(self):
        self.get_data()
        self.put_data()
    def get_data(self):
        super().get_data()              # Super Function will automatically inherit the properties from its First Parent Class.
        super(Publication, self).get_data()     # Here, it will call all constructors after Publication.
        self.time=float(input("Enter the Playing Time in Minutes: "))
    def put_data(self):
        super().put_data()     
        super(Publication, self).put_data()
        print("The Playing Time in Minutes is: ",self.time)
        print("______________________________________")

# Driver Program
# Creating Instances of Book and Tape Classes.

My_Book=Book()
My_Tape=Tape()



