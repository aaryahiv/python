
def circumference (radius):
    c = 2 * 3.14 * radius
    return c

def area (e):
    a = 3.14 * e**2
    return a

def diameter (y):
    d = 2 * y
    return d

print("Start of program")
r = input("Enter radius of your circle:")
r = int(r)
circum = circumference(r)
area1 = area(r)
diameter1 = diameter(r)
print("The circumference is", circum)
print("The area is", area1)
print("The diameter is", diameter1)
print("End of program")


    
    
