# Programming Fundamentals (Lab)
# Clsses-Object Oriented Programming
# Date: 11th August 2020
# Submitted By: Sundas Noreen


class Rectangle(object):   # Class Definition for Rectangle.
     """
     Represents a Rectangle.
     Attributes of the Class: x, y, width, height
    """
     pass

def Create_Rectangle (x, y, width, height):  # This Function takes 4 attributes and Creates a New Instance of Rectangle.
    a = Rectangle()           # A Call to Class Rectangle.
    a.x = x
    a.y = y
    a.width = width
    a.height = height
    return a           # Return Width, Height and values of Ponts x and y of Rectangle.
    
def Str_Rectangle(Rect): # Convert given Rectangle instance into string of form.
    return "(%g, %g, %g, %g)" % (Rect.x, Rect.y, Rect.width, Rect.height)   # Converting Instances to String.
                               
def Shift_Rectangle(Rect,dx,dy): # Change the x and y coordinates of the given Rectangle instance.
    Rect.x+=dx
    Rect.y+=dy
        
def OffSet_Rectangle(Rect,dx,dy): # Create a new Rectangle instance which is offset by dx and dy.
    x=Rect.x+dx
    y=Rect.y+dy
    Instances=Create_Rectangle (x, y, Rect.width, Rect.height)
    return Instances

# Running the Code.
r1 = Create_Rectangle(10, 20, 30, 40)
print(Str_Rectangle(r1))
Shift_Rectangle(r1,-10,-20)
print(Str_Rectangle(r1))
r2 = OffSet_Rectangle(r1, 100, 100)
print(Str_Rectangle(r1))
print(Str_Rectangle(r2))

# Function to find the signed difference in area between two Rectangle Instances.
def Area_Difference(r1, r2):
    area1 = r1.width * r1.height
    area2 = r2.width * r2.height
    difference= area1-area2
    return difference

# Running the Code.
r1 = Create_Rectangle(10, 20, 10, 10)
r2 = Create_Rectangle(20, 50, 15, 20)
print("\n",Area_Difference(r1, r2))





