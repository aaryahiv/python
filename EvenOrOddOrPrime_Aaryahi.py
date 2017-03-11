#EvenOrOddOrPrime
print("Start of program")
number=input("How many numbers do you want?")
number = int(number)
for x in range(2,number+1):
    y = x % 2
    if (y == 0):
        print("Even number is",x)

    if (y == 1):
        print("Odd number is",x)
