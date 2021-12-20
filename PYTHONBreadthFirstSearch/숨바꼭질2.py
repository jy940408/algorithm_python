from collections import deque

startNum, goalNum = map(int, (input()).split())

board = [-1 for i in range(100001)]
visitList = [-1 for i in range(100001)]
visitList[startNum] = 1

bfsDeque = deque()
bfsDeque.append([startNum, 0])

resultLen = 0
resultNum = 0
if startNum == goalNum:
    resultNum = 1
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
            if visitList[subRoot] == -1 or visitList[subRoot] == (thisDeque[1]+1):
                visitList[subRoot] = (thisDeque[1]+1)
                bfsDeque.append([subRoot, (thisDeque[1]+1)])
                
            if subRoot == goalNum and visitList[subRoot] == (thisDeque[1]+1):
                print(thisDeque[0])
                resultLen = visitList[subRoot]
                resultNum += 1

print(resultLen)
print(resultNum)