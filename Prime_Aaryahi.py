print("Start of program")

password = input("Enter the password:")
if(password == "Aaryahi" or password == "Vandu"):

    howold = input("Enter your age:")
    howold=int(howold)
    if(howold == 8 or howold == 10):
        print("Welcome")


        number = input("Enter the prime number you want to chose:")
        number = int(number)
        answer = 0
        for other in range(1,number+1):
            number2 = other % 2
            if(number2 != 0):
                print("Prime number is",other)
                answer = answer + other
        print("The sum of the prime numbers up to", number,"is",answer)

                



    else:
        print("Age Incorrect,Get out!")


else:
    print("Password Wrong!")
