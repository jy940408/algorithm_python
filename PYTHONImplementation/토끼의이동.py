length, turn = map(int, input().split())
testCase = list(input())

upDown = [1, 0, -1, 0, 0]
leftRight = [0, 0, 0, -1, 1]

thisLocation = [1, 1]
result = 1
for i in testCase:
    
    thisLocation[0] += upDown[(ord(i)-68)%5]
    thisLocation[1] += leftRight[(ord(i)-68)%5]

    lineNum = ((thisLocation[0] + thisLocation[1]) - 1)
    if lineNum < (length+1):
        lineStart = ((lineNum*(lineNum-1)//2))
        if lineNum%2 == 0:
            result += (lineStart + thisLocation[0])
        else:
            result += (lineStart + (lineNum-(thisLocation[0]-1)))

    else:
        thisNum = (2*length-lineNum)
        lineStart = ((length*(length+1))//2) + ((length*(length-1))//2 - (thisNum+1)*thisNum//2)
        subLocation = (thisLocation[0] - (lineNum-length))
        if lineNum%2 == 0:
            result += (lineStart + subLocation)
        else:
            result += (lineStart + (thisNum-(subLocation-1)))

print(result)