word = input()
for letter in word:
    if(letter == letter.upper()):
        print(letter.lower(), end = '')
    if(letter == letter.lower()):
        print(letter.upper(), end = '')
