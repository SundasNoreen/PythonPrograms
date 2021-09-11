#Tuples and List by Sundas Noreen
#Writing a function that emulates the builtin zip function.
#It will take  iterables and return a list of tuples.
#Each tuple will contain one element from each of the iterables passed to the function.

def My_Function(x,y):               # Defining the Function with two Input Parameters.
    Record_List=[]                  #A list that will be holding the tuples returned.It is initially empty.
    for i in range(len(x)):         #Iterating over one parameter.
        Tuple=(x[i],y[i])           #writing a tuple with corresponding elements from each parameter.
        Record_List.insert(i,Tuple) #Insert tuple to the Record_List.
    return Record_List              #Return the Record List.

result=My_Function([1,2,3],'abc')  #calling the Function
print(result)                      #Printing the Result



