"""
inputList = [""]*100
count = 0
num1 = input()
num1 = int(num1)
num2 = input()
num2 = int(num2)
num3 = input()
num3 = int(num3)
for x in range(num1,num2+1):
    if(x % num3 == 0):
        #print("Numbers:",x)
        inputList[count] = x
        count = count + 1
print("Count:",count)
print("List:",inputList)
"""
count = 0
numbers = input()

numList = numbers.split()
num1 = numList[0]
num2 = numList[1]
num3 = numList[2]


#num1, num2, num3 = numbers.split()
num1 = int(num1)
#num2 = input()
num2 = int(num2)
#num3 = input()
num3 = int(num3)
for x in range(num1,num2+1):
    if(x % num3 == 0):
        count = count + 1
print(count)

        
        
        

