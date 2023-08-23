# Dictionary values can be of any datatypes
#but there is a rule called dictionary keys that they myst be immutable
# Dictionary keys cannot contain any mutable type directly or indirectly

data = {1: "hello", 2:"world"} #valid
data = {2.1: [1,2,3], True:"Hello"} #valid
data = {(1,2,3):1, (4,5): 2} #valid
#data= {([1,2,3],2): "Hello", 2:"world"} #invalid
#data = {[1, 2, 3]: "Hello", 2: "World"}  # Invalid

student = {"name": "Jon", "address": "KTM"}  # Valid


#####Membereship in dictionary is observed  in keys and not in values
student = {"name":"jon", "address":"KTM"}
print("jon" in student) #false
print("name" in student) #true