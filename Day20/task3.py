"""
Create a dictionary student with keys id, name, age, department. 
Take a input from the user, which info (id, name, age or department)
he wants to access and print the result. Handle the possible exceptions.

"""
student={
    "name" : "Ram",
    "id": 123,
    "age": 23,
    "department": "science"
}
try:
    key = input("Enter your info which you want to enroll")
    result = student[key]
except KeyError:
    print("Please provide valid key!!")
else:
    print(f"The {key} of the student is {result}")
