startWord = input()
goalWord = input()

while len(startWord) < len(goalWord):
    if len(startWord) < len(goalWord):
        if goalWord[len(goalWord)-1] == "A":
            subWord = ""
            for i in range(len(goalWord)-1):
                subWord += goalWord[i]
            goalWord = subWord
            
        else:
            subWord = ""
            for i in range(len(goalWord)-2, -1, -1):
                subWord += goalWord[i]
            goalWord = subWord

if startWord == goalWord:
    print(1)
else:
    print(0)