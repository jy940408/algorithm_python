wordNum = int(input())
wordList = [input() for i in range(wordNum)]

result = 0
for i in range(wordNum-1) :
    for j in range(i+1,wordNum) :
        startWord = wordList[i]
        goalWord = wordList[j]

        subCheck =True
        if len(startWord) == len(goalWord):
            firstVisit = [0]*26
            secondVisit = [0]*26
            
            for k in range(len(startWord)):
                firstIdx = ord(startWord[k]) - ord('a')
                secondIdx = ord(goalWord[k]) - ord('a')
                
                if firstVisit[firstIdx] == 0 and secondVisit[secondIdx] == 0:
                    firstVisit[firstIdx] = goalWord[k]
                    secondVisit[secondIdx] = startWord[k]

                elif firstVisit[firstIdx] != goalWord[k]:
                    subCheck=False
                    break
                
        if subCheck:
            result+=1        

print(result)