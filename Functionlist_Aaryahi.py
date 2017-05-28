
#Reference
listinput = [""]*1000
def listfunction():
    a = 0
    number = input("Enter a number or print:")
    while(number != "print"):
        listinput[a] = number
        a = a + 1
        number = input("Enter a number or print:")
    return listinput,a
    
def printFunction(list1,j):
    for y in range(0,j):
        print(list1[y])
    return
    

#Main Program
print("Start or program")
x,index = listfunction()
printFunction(x,index)
print("End of program")





