roundNum = int(input())

for i in range(roundNum):
    length = int(input())
    wordList = list(map(str, input().split()))
    
    result = [wordList[0]]
    for i in range(1, len(wordList)):
        left = wordList[0]
        right = result[-1]
        
        if wordList[i] <= left:
            result.insert(0, wordList[i])
        else:
            result.append(wordList[i])
    
    output = ""
    for j in result:
        output += j

    print(output)    