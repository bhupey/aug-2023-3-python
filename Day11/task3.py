"""
Write a program to prompt for a score between 0.0 and 1.0. If the score is between 0.0 and 1.0, print a grade using the following table: 
A for >=0.9
B for >=0.8
C for >=0.7
D for >=0.6
F for <0.6

If the user enters a value out of range, print a suitable error message.

"""
marks = float(input("Enter marks:"))
if marks>=1 or marks<0:
    print("invalid number")
elif marks>=0.9:
    print("A")
elif marks>=0.8:
    print("B")
elif marks>=0.7:
    print("C")
elif marks>=0.6:
    print("D")
elif marks<0.6:
    print("F")
