# like any other programming language python also has its own set of operators
# operators are the symbols used to carry out mathematical and logical operations
# operatrs in python are :
# 1. Arthimetic Operators
# 2. Logical Operators
# 3. Relational/ Comparision Operators
# 4. Assignment Operators
# 5. Membership Operators
# 6. Identity Operators


### Arthimetic Operators ###
# addition (+)
a= 1
b=2
c= a+b
print(c)

# subtraction (-)
a= 1
b=2
c= a-b
print(c)

# Multiplication (*)
a= 1
b=2
c= a*b
print(c)

#raise to the power
a= 1
print( a**3)

#Division (/)
a= 1
b=2
c= a/b
print(c)

#remainder / Modulus(%)
a= 1
b=2
print(a % 2)
print(b %2)

#floor division(//)
a = 3
print(a/2) #1.5
print(a // 2) #1

a = -3
print(a/2) # -1.5
print(a // 2) # -2


###Relational Operators####
#  >,<,==, >=, <=, != are the relational operators
# result of the relational operations are true/false
a = 5
b = 2
print(a > b) #True
print(a < b) #false
print(b > a) #false
print (b < a) #true
print(a == b) #false
print(a <= b) #false


### Logical Operators
# and, or, not are the logical operators in python
# result of the logical operations are true/false

a = 5
b = 3
c = 5

print (a==c or a==b) #True
print (a==c and a==b) #False
print (a!=c or a==b) # False

a = True
print(not a) #False

a = 5
print(not a) #False


### Assignment Operator ####
# "=" is the basic assignment operator
institude = "Broadway" # here = is the assignment operator


###Membership operator##
# 'in' and 'not in' are the membership operator
# the result of  membership operation us also true / false

print(2 in [1,2,3]) # true
print(3 not in [1,2,3]) #false


###Identity OPerators###
