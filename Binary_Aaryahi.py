
def binary(binary1):
    binaryList = []
    addition = 0
    for x in binary1:
        x = int(x)
        binaryList.append(x)
    length = len(binaryList)
    for index in range(0, length):
        addition = addition + (binaryList[index]*(2**(length-index-1)))
    print(addition)
    return


print("Main Program")
binaryNum = input("Enter a binary number or quit:")
while(binary != "quit"):
    binary(binaryNum)
    binaryNum = input("Enter a binary number or quit:")
print("End of program")

