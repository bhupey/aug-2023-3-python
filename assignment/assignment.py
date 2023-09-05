"""
1. Write a Python program that accepts an integer (n) and computes the value 
of n+nn+nnn + …
"""

num = int (input("Enter any number: "))
if num < 10:
    new_num = 0
    total = 0
    for _ in range(num):
        new_num = new_num*10+num
        total += new_num
else:
    print("It is valid only for single digit number")
print(total)



"""
2. Write a Python program to calculate the difference between a given 
number and 17. If the number is greater than 17, return twice the absolute 
difference


num = int(input("Enter any number: "))
difference = abs(num - 17)
if num>17:
    result = 2*difference
else:
    result= difference
print(f"The result is: {result}")
"""


"""
3. Write a Python program to check whether the input number is prime or 
not.

num = int (input("Enter a number: "))
if num < 2:
    prime = False
else:
    prime = True

for i in range(2, num):
    if num%i == 0:
        prime = False
        break

if prime:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")

"""