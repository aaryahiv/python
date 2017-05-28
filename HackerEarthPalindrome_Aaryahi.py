originalCount = 0
reverseCount = 0
s = input()
inputListRev = [""]*len(s)
inputListOrig = [""]*len(s)

if(len(s) >= 1) and (len(s) <= 100):
    
    for letter in s:
        inputListOrig[originalCount] = letter
        originalCount = originalCount + 1

    for letter in s:
        inputListRev[(len(s)-1)-reverseCount] = letter
        reverseCount = reverseCount + 1

    if(inputListRev == inputListOrig):
        print("YES")
    else:
        print("NO")


