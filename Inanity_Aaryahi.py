
def inanity(numf, numd):
    numdList = []
    remainderList = []
    total = 0
    numd = numd.strip()
    numdList = numd.split(" ")
    for x in numdList:
        x = int(x)
        remainder = x % numf
        remainderList.append(remainder)
        total = total + remainder
    print(total)
    return

print("Main Program")
numf = input()
numf = int(numf)
numd = input()
inanity(numf, numd)
print("End of program")
    
