# True and False are the boolean types in python
# True and False are also the keywords in python

# Operations that give boolean types

a= 5
b= 10
c= 25

#relational operations
print(b>a) #True
print(b!= a) #True
print(b < a) # False
print(a=c) #False

#Logical operations
print(b>a and a==c) #False
print(b>a or a==c) #True
print(not True) #False
print(not False) #True
print(not a) #False

# Membership operations
print(2 in [1,2,3]) #True
print(5 in [1,2,3]) #False


#Identity Operation
a = 1
b = 1
print(a==b) #True
print(a is b) #True


a = 123456 # it is created in one memory location
b = 123456 # but it is created in another memory location
print(a==b) #True
print(a is b) #False 


#concept of truthly and falsy
#truthly
# all non-empty data types and non-zero number are truthy values
a = 12
b = 5.7
c = [1,2]
d = (2,3)
e = {5,6}
f = True
# all these datatypes are truthly datatypes
# we can check the truthiness of the data using bool function

print(bool(b)) #True


#Falsy
# all empty data types and zero number are falsy values
a = 12\
b = 5.7
c = [1,2]b
d = (2,3)
e = {5,6}
f = False
g = None
# all these datatypes are falsy datatypes
# we can check the falsy of the data using bool function

print(bool(f)) #False

#python booleans are the subclass of the integer class. That means True is 1 and False is 0
a = True
b = 3
print(a+b) #4
print (70*False) #0
print (True+True) #2 

