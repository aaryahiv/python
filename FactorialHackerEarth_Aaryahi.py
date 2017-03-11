num = input()
num = int(num)
print("DEBUG:",num)
for x in range(num-1,0,-1):
    num = num * x
    print("DEBUG:",x,num)
print(num)
    
