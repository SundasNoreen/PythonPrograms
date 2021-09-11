#   Lab Assignemnt on "DICTIONARIES" 
#   Task 3
#   Submitted By: SUNDAS NOREEN

lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}

alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}

tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Creating a list called 'students' that contains lloyd, alice, and `tyler.
students=[lloyd, alice, tyler]

# Printing the Student's Data.
print("\nStudent's Details")
for each in students:
    print("\nName: ",each["name"])
    print("Homework: ",each["homework"])
    print("Quizzes: " ,each["quizzes"])
    print("Tests: ",each["tests"])
print("__________________________________________")

# Getting Average of Student's Marks.    
def average (numbers):
    total=sum(numbers)
    total=float(total)
    length_of_list=len(numbers)
    avg=total/length_of_list
    return avg

# Taking Average of Overall marks scored by a student.
def get_average (student):
    homework= average(student["homework"])
    quizzes= average(student["quizzes"])
    tests= average(student["tests"])
    a= (homework*10)/100
    b= (quizzes*30)/100
    c= (tests*60)/100
    overall= a+b+c
    return overall

# Function to Mark Student's Grades based on his overall average marks.
def get_letter_grade (score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"
# Testing the Functon.
print("\nGrade of 'Lloyd' is: ",get_letter_grade(get_average(lloyd)))
    
# Function that will iterate over the students list and will return his average marks & will be stored in a list.
def get_class_average(students):
      results=[]
      for student in students:
          z=get_average(student)
          results.append(z)

      return average(results)
  
final_avg=get_class_average(students)     # Calling get_class_average function to iterate over the list 'students'.
print("\nAverage marks of students [Lloyd, Alice, Tyler] are = ",final_avg)

final_grades=get_letter_grade(final_avg)  # Calling get_letter_grade function to calculate the overall grade of all students.
print("\nGrade for Class Average Score is: ",final_grade)
print("__________________________________________")


