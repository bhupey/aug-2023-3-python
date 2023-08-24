# methods are also functions but methods are the function inside class
# methods must be called with object

"""def addition(a, b): #function defenation
    return a+b
#here addition is just a function but not a method
result = addition(2,3)  #function call
print(result) #5


class Student:
    def get_age_after_10_years(self, current_age):
        return current_age+10
    
    Student = Student()
    result = student.get_age_after_10_years(21)
    print(result)  #31
    # here get_age_after_10_years is a method """


    ##########List Method########

    #append()
vowels = ["a", "e", "i", "o"]
vowels.append("u")
print(vowels)  #["a", "e", "i", "o", "u"]

    #extend()
data = [1,2,3,4]
data.extend([5,6,7,8])
print(data)  #[1,2,3,4,5,6,7,8]



#insert()
vowels = ["a", "e", "o", "u"]
vowels.insert(2, "i")
print(vowels)  #["a", "e", "i", "o", "u"]

#remove()
vowels = ["a", "e", "o", "u"]
vowels.remove("o")
print(vowels)

#vowels.remove("z") #this raises erroe: value error

#pop()
vowels= ["a", "e", "i", "o", "u"]
result=vowels.pop()
print(result) #u
print(vowels) # ["a", "e", "i", "o"]
result= vowels.pop(1) # we can also give index as parameter
print(result) #e
print(vowels) #["a", "i", "o"]

#clear
vowels.clear()
print(vowels) #[]


#index method
vowels= ["a", "e", "i", "o", "u"]
result= vowels.index('e')
print (result) #1
print(vowels) #["a", "e", "i", "o", "u"]



#count
data = [1,2,2,5,5,3,5,3,4,2]
result = data.count(2)
print(result)  #3


# copy()
a = [1,2,3]
b = a
print(a) #[1,2,3]
print(b) #[1,2,3]
print(a is b) #True. They are the same objects


b = a.copy()
print(a) #[1,2,3]
print(b) #[1,2,3]
print(a is b) #False. 'a' and 'b' are diffrent objects



a = [[1,2,3],4]
b = a.copy()
a[0][1] = 7
print(a) #[[1,7,3],4]
print(b) #[[1,7,3],4]
#here 'b' is a shallow copy of 'a'. Mutable objects are still the same object in both 'a' and 'b'


#shallow copy
#we can overcome this using deepcopy

from copy import deepcopy
a = [[1,2,3],4]
b = deepcopy(a)
a[0][1] = 7
print(a)  # [[1, 7, 3], 4]
print(b)  # [[1, 2, 3], 4]






    