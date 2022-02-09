goalNum, resultNum = map(int, input().split())

result = 0
thisLength = 1
rangeLength = 9

while resultNum > thisLength*rangeLength:
    resultNum -= (thisLength*rangeLength)
    result += rangeLength
    thisLength += 1
    rangeLength *= 10

result = (result+1)+(resultNum-1)//thisLength

if result > goalNum:
    print(-1)
else:
    print(str(result)[(resultNum-1)%thisLength])