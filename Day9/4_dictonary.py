# Dictonary are the mutable datatypes in python
# they are the key-value pairs enclosed within curly braces
# creating a empty dictonary

a = {}
print(a)
a = dict()
print(a)

#Creating non-empty dictionary
student = {"name":"jane", "age": "30", "address": "KTM"}
print (student)

student = dict(name="jane", age=30, address="KTM")
print(student)



#accessing elements of a dictionary
#Dicrionary elements are accesed using keys
student = {"name":"jane", "age": "30", "address": "KTM"}
name = student["name"]
print(name) #jane

age = student["age"]
print(age) #30


#Accessing dictionary elements by using .get() method
student = {"name":"jane", "age": "30", "address": "KTM"}
name = student.get("name")
print(name) #jane

roll_no = student.get("roll_no")
print(roll_no) # none

