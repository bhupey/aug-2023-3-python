a = 1
print(type(a))  #int

a = (1)
print(type(a))  #int

a = (1,)
print(type(a))  #tuple

a = 1,
print(type(a))  #tuple. And this a tuple packing

a= 1,2,3
print(a)  #(1,2,3)  #This is the example of tuple packing


a,b,c = 1,2,3  #THis is the example of unpacking
print(a) #1
print(b) #2
print(c) #3

a,b,c = (1,2,3)  #THis is the example of unpacking
print(a) #1
print(b) #2
print(c) #3

#Possible errors in tuple packing and unpacking
# If the number of elements in LHS is not equals to the number of elements in RHS, then it raises error

a,b = 1,2,3 #toomany values to unpack
a,b,c = 1,2 #not enough values to unpack

