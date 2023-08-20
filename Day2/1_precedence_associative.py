# precedence is the order in which operations are carried out
# multiple operators can have same precedence in such that case associative is concidered.
#Normally associativity order is from left to right except for the case of **

a = 3-2+1
#here 3-2 is first caluculated and the result is added with 1

# but for '**' associativity is from right to left
a=2**2**3
print(a) #256