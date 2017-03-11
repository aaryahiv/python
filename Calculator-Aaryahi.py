#Calculator.py

print("Start of program")

x = input("Enter your first number:")
x = int (x)
y = input("Enter your second number:")
y = int (y)
calculate=input("Do you want to +, -, *, or /:")

if(calculate == "+"):
    a = y + x
if(calculate == "-"):
    a = y - x
if(calculate == "*"):
    a = y * x
if(calculate == "/"):
    a = y / x

print ("The calculated number of both numbers is", a)

print("End of program")
