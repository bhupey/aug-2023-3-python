"""
Take two numbers input and divide a number by another number.
 Handle the possible exceptions.

"""

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter second number: "))
    print((num1 / num2))

except ZeroDivisionError:
    print("Please do not divide by zero")

except Exception as e:
    print(e)


    
    
