# Programming Fundamentals Lab
# Task on Inheritance (Part-1)
# Date: 18th August 2020
# Submitted By: Sundas Noreen

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

class Book(Publication):        # Child Class derived from Class Publication.
    def __init__(self):
        self.get_data()
        self.put_data()
    def get_data(self):
        super().get_data()      # Super Function will automatically inherit the properties from its Parent Class.
        self.page=int(input("Enter the Page Count: "))
    def put_data(self):
        super().put_data()
        print("The Page Count is: ",self.page)
        print("______________________________________")

class Tape(Publication):        # Child Class derived from Class Publication.
    def __init__(self):
        self.get_data()
        self.put_data()
    def get_data(self):
        super().get_data()
        self.time=float(input("Enter the Playing Time in Minutes: "))
    def put_data(self):
        super().put_data()      # Super Function will automatically inherit the properties from its Parent Class.
        print("The Playing Time in Minutes is: ",self.time)
        print("______________________________________")

# Driver Program
# Creating Instances of Book and Tape Classes.

My_Book=Book()
My_Tape=Tape()





