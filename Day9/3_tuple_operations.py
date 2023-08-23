# Concatenation (+)

a = (1,2,3)
b = (4,5,6)
print(a+b) #(1,2,3,4,5,6)


#Repetition(*)

a = (1,2)
print(a*2) #(1,2,1,2)


#Membership Operation ("in" and "not in")

a=(1,2,3)
print (2 in a) #True




#Some function that can be used with tuple

a = (1,2,3,4,5)
print(sum(a)) #15

print(max(a))  #5
print(min(a))  #1


a = (5,2,4,3,1)
result = sorted(a)
print(result)  #[1,2,3,4,5]


result= reversed(a)
print(list(result)) #[1,3,4,2,5]     
