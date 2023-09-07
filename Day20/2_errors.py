# Thera are broadly two types of errors in any programming language:
# 1. Syantax Error
# 2. Non-syntactic Error


# syantax Error
# This type of errors occur when we mess up with the grammar of the programming language
#Example
# a =   #Incomplete code
# if a:
# print("a") #If block without indentation etc. are the syntac error of python language




# 22. Non- syntactic Error
# All other errors except syntac error fall in this category
# These errors can further be classified as:
# 1. TypeError
# 2. ValueError
# 3. ZeroDivisionError
# 4. NameError
# 5. ModuleNotFoundError
# 6. IndexError
# 7. KeyError

# 2 + "Hello"   # TypeError
# int("Hello")  # ValueError
# 3 / 0  # ZeroDivisionError

# a = 1
# print(b)  # Name b is not defined. NameError

# import jason  # No module named jason. ModuleNotFoundError

# a = [1, 2, 3, 4]
# print(a[5])  # IndexError

student = {"name": "ABC", "age": 20}
print(student["id"])   # KeyError
print(student.get("id"))  # None