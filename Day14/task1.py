"""
WAP to delete all the occurrences of a specified character in a given string 
S = “All the occurrences of a specified character in a given string”
Input = “a”
Output = “ll occurrences of  specified chrcter in  given string”

"""
S = "All the occurrences of a specified character in a given string"
char = input("Enter the letter you want to ommit: ")
result = ""
for each in S:
    if each.lower() == char.lower():
        continue
    result += each 
print(result)