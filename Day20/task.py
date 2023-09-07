"""
Take two numbers as input and add those numbers. Handle the possible exceptions.
"""

try:
    num1 = int (input("Enter a number: "))
    num2 = int (input("Enter second number: "))
except Exception as e:
    print( "Error")

else:
    print(num1 + num2)
