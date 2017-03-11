print("Start of program")
count = 0
word = input("Enter a word:")
wordList = [""]*len(word)
for letter in word:
    wordList[count] = letter
    count = count + 1

print(wordList)


index = 0
b = ""
while(index != len(word)-1):
    for x in range(index,len(word)):
        if(wordList[index] > wordList[x]):
            b = wordList[index]
            wordList[index] = wordList[x]
            wordList[x] = b
        else:                                          
            pass
    index = index + 1

print(wordList)

#print(index,"Lowest Letter is ", wordList[index])

y = "".join(wordList)
print(y)

print("End of program")
