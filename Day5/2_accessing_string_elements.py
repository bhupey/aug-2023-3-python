# Indexing
# We can access string elements using indexing and slicing which is similar to the list
# forward indexing starts from 0 and reverse indexing from -1

message = "Hello World"
print(message[1]) #e
print(message[5]) #space
print(message[-1]) #d


#Slicing
message = "I am learning python"
print(message[:6]) # 'space am space'
print(message[0:5]) # 'I space am space'
print(message[3:8]) # 'm space lea'
print(message[4:])  # 'learning python'
print(message[7:2]) # empty ''
print(message[-8:-2]) #'g space pyth'
print(message[-6:-8]) #empty ''
print(message[3:-3]) #'m learning pyt'
print(message[9:-11]) #empty ''


#Creating the object (empty and non empty)
# accessing the elements (Indexing/ slicing/ accessing element using key)
# operations
# methods
# Built in function


"""
message = "Hello"
message[2] = "L"
print(message)    #error. it is not possible because string is immutable

"""

