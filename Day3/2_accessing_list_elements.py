# list elements are accesed using indexing and slicing

# Indexing
# Indexing in python starts from 0 for forward indexing and -1 for reverse indexing
vowels = ["a", "e", "i", "o", "u"]
print(vowels[0]) #"a"
print(vowels[3]) #"o"
#print(vowels[5]) #"Error"

print(vowels[-1]) #"u"
print(vowels[-4]) #"e"
#print(vowels[-6]) #Errorss



#slicing

Data = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(Data[:])  #["a", "b", "c", "d", "e", "f", "g", "h"]
print(Data[2:7])  #"c", "d", "e", "f", "g"
print(Data[4:7])  #"e", "f", "g"
print(Data[:7])   #"a", "b", "c", "d", "e", "f", "g"
print(Data[-8:-2])  #"a", "b", "c", "d", "e", "f"
print(Data[-4:])  #["e", "f", "g", "h"]

print(Data[1:7:2])  #["b", "d", "f", ]