def write ():
    outFile = open("students.txt","a")
    n = input("Enter student name:")
    m = input("Enter math score:")
    h = input("Enter history score:")
    c = input("Enter coding score:")
    outFile.write(n+"'s math score is "+m+", history score is "+h+", coding score is "+c+"\n")
    outFile.close()
    return

def read ():
    outFile = open("students.txt","r")
    lines = outFile.read().split("\n")
    for line in lines:
        print(line)
    outFile.close()
    return 

def indiScore ():
    outFile = open("students.txt","r")
    i = input("Enter name:")
    lines = outFile.read().split("\n")
    for line in lines:
        if(i in line):
            print(line)
            break
        else:
            continue
    outFile.close()
            

print("Start of program")
select = input("1 to add to file and 2 to read file and 3 for individual student scores or quit:")
while(select != "quit"):
    if(select == "1"):
        write()
    elif(select == "2"):
        read()
    elif(select == "3"):
       indiScore()
    else:
        print("Invalid selection, please enter again")
    select = input("1 to add to file and 2 to read file and 3 for individual student scores or quit:")
print("End of program")

    

       
        
        
