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
