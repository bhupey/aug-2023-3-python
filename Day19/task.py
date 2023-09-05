"""
Create a class Department with parameters name and number_of_students. 
Create a method total students, which takes object as a parameter and return the
total number of students from all departments.

"""


class department:
    
    def __init__(self, name, number_of_student):
        self.name = name
        self.number_of_student = number_of_student
        

    def total_student(self, other):
        return self.number_of_student + other.number_of_student
    
    
d1 = department("Math department", 50)
d2 = department("science department", 90)
total = d1.total_student(d2)
print(total)

