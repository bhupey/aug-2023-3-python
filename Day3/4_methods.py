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




    