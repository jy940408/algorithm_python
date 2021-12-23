from collections import deque

startNum, goalNum = map(int, (input()).split())

visitList = [-1 for i in range(100001)]
visitList[startNum] = startNum

bfsDeque = deque()
bfsDeque.append([startNum, 0])

resultLen = 0
resultString = str(goalNum)

breakCheck = False
while bfsDeque:
    thisDeque = bfsDeque.popleft()
    
    for i in range(3):
        subRoot = 0
        if i == 0:
            subRoot = (thisDeque[0] + 1)
        elif i == 1:
            subRoot = (thisDeque[0] - 1)
        else:
            subRoot = (thisDeque[0]*2)
    
        if 0 <= subRoot < 100001:
            if visitList[subRoot] == -1:
                visitList[subRoot] = thisDeque[0]
                if subRoot == goalNum:
                    resultLen = (thisDeque[1]+1)
                    breakCheck = True
                    break
                
                bfsDeque.append([subRoot, (thisDeque[1] + 1)])
    
    if breakCheck:
        break

resultGoal = goalNum
while resultGoal != startNum:
    resultGoal = visitList[resultGoal]
    resultString = str(resultGoal) + " " + resultString

print(resultLen)
print(resultString)