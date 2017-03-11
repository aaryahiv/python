def add ():
    outFile = open("highestAdd.txt","a")
    n = input("Enter a name or quit:")
    while(n != "quit"):
        m = input("Enter math score:")
        h = input("Enter history score:")
        s = input("Enter science score:")
        outFile.write(n+" , "+m+" , "+h+" , "+s+"\n")
    n = input("Enter a name or quit:")
    outFile.close()
    return

def read ():
    outFile = open("highestAdd.txt","r")
    n = input("Enter a name or quit:")
    while(n != "quit"):
        outFile.seek(0)
        lines = outFile.read().split("\n")
        for line in lines:
            line2 = line.split(' , ')
            if n in line:
                #print("DEBUG: ",line)
            break
        print(line)
        n = input("Enter a name or quit:")
    outFile.close()
    return

def highestMathScore ():
    outFile = open("highestAdd.txt","r")
    highest = 0
    lines = outFile.read().split("\n")
    for line in lines:
        if line:
            l = line.split(" , ")
            math = int(l[1])
            if(highest < math):
                highest = math
            else:
                pass
        else:
            pass
    print(highest)
    outFile.close()
    return

print("Start of program")
select = input("1 to add to file, 2 to read a student's scores, 3 to find highest math score or quit:")
while(select != "quit"):
    if(select == "1"):
        add()
    if(select == "2"):
        read()
    if(select == "3"):
        highestMathScore()
    select = input("1 to add to file, 2 to read a student's scores, 3 to find highest math score or quit:")
print('End of program')

    
