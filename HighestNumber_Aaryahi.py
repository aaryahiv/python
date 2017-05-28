
print("Start of program\n")

list1 = [""]* 10000
number = input("Enter a number or quit:")
index = 0
high = 0
while(number != "quit"):

    number = int(number)

    if(number > high ):
        high = number
    list1[index] = number
    index = index + 1


    number = input("Enter a number or quit:")
        

for y in range(0,index):
    print(list1[y])
print("This is the highest number from your list:",high)
print("\nEnd of program")
    
    
